from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import Category, Escalation, Notification, ReopeningRequest, Role, Ticket, TicketActivity, WorkNote
from .permissions import IsAdministrator, is_support, role_of
from .serializers import (CategorySerializer, EscalationSerializer, NotificationSerializer, TicketCreateSerializer,
                          TicketDetailSerializer, TicketListSerializer, UserSerializer, WorkNoteSerializer)


def activity(ticket, actor, event_type, **details):
    TicketActivity.objects.create(ticket=ticket, actor=actor, event_type=event_type, details=details)


def notify(recipient, ticket, event, message):
    if recipient:
        Notification.objects.create(recipient=recipient, ticket=ticket, event=event, message=message)


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    user = authenticate(username=request.data.get("username", ""), password=request.data.get("password", ""))
    if not user or not user.is_active:
        return Response({"detail": "Invalid username or password."}, status=status.HTTP_401_UNAUTHORIZED)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user": UserSerializer(user).data})


@api_view(["POST"])
def logout_view(request):
    request.auth.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def me_view(request):
    return Response(UserSerializer(request.user).data)


@api_view(["GET"])
def support_users_view(request):
    """Return active technicians/supervisors for ticket assignment."""
    if not is_support(request.user):
        return Response({"detail": "Support role required."}, status=403)
    users = User.objects.filter(is_active=True, profile__role__in=[Role.TECHNICIAN, Role.SUPERVISOR]).select_related("profile").order_by("first_name", "username")
    return Response(UserSerializer(users, many=True).data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def get_permissions(self):
        return [IsAuthenticated()] if self.action in ("list", "retrieve") else [IsAdministrator()]


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.select_related("requester", "requester__profile", "assignee", "assignee__profile", "category").prefetch_related("activities__actor", "work_notes__author", "escalations__created_by", "escalations__internal_owner", "reopening_requests__requester")

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if not is_support(user) and role_of(user) != Role.REPORT_VIEWER:
            qs = qs.filter(requester=user)
        params = self.request.query_params
        for field in ("status", "priority", "category", "assignee"):
            if params.get(field): qs = qs.filter(**{field: params[field]})
        if params.get("q"):
            qs = qs.filter(Q(reference__icontains=params["q"]) | Q(title__icontains=params["q"]))
        return qs

    def get_serializer_class(self):
        if self.action == "create": return TicketCreateSerializer
        if self.action == "retrieve": return TicketDetailSerializer
        return TicketListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        ticket = serializer.save()
        return Response(TicketDetailSerializer(ticket, context={"request": request}).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=["post"])
    def assign(self, request, pk=None):
        if role_of(request.user) != Role.SUPERVISOR:
            return Response({"detail": "Only the Technical Supervisor can assign tickets."}, status=403)
        ticket = self.get_object(); assignee_id = request.data.get("assignee")
        assignee_name = request.data.get("assignee_name", "").strip()
        if assignee_name:
            assignee = User.objects.filter(
                Q(username__iexact=assignee_name) |
                Q(first_name__iexact=assignee_name) |
                Q(last_name__iexact=assignee_name) |
                Q(first_name__iexact=assignee_name.split(" ")[0], last_name__iexact=" ".join(assignee_name.split(" ")[1:])),
                is_active=True,
                profile__role=Role.TECHNICIAN,
            ).select_related("profile").first()
            if not assignee:
                return Response({"detail": "No active technician was found with that name or username."}, status=400)
        else:
            try: assignee = User.objects.get(pk=assignee_id, is_active=True)
            except User.DoesNotExist: return Response({"detail": "Enter the technician's name or username."}, status=400)
        if role_of(assignee) != Role.TECHNICIAN: return Response({"detail": "Assignee must be an active technician."}, status=400)
        old = ticket.assignee_id; ticket.assignee = assignee
        if ticket.status in {Ticket.Status.SUBMITTED, Ticket.Status.OPEN}: ticket.status = Ticket.Status.ASSIGNED
        ticket.save(); activity(ticket, request.user, "ASSIGNED", previous_assignee=old, assignee=assignee.id, entered_name=assignee_name)
        notify(assignee, ticket, "TICKET_ASSIGNED", f"{ticket.reference} has been assigned to you.")
        return Response(TicketDetailSerializer(ticket, context={"request": request}).data)

    @action(detail=True, methods=["post"])
    def update_workflow(self, request, pk=None):
        if not is_support(request.user): return Response({"detail": "Support role required."}, status=403)
        ticket = self.get_object(); new_status = request.data.get("status"); resolution = request.data.get("resolution", "")
        allowed = {Ticket.Status.ASSIGNED, Ticket.Status.IN_PROGRESS, Ticket.Status.WAITING, Ticket.Status.ESCALATED, Ticket.Status.RESOLVED, Ticket.Status.CLOSED, Ticket.Status.OPEN}
        if new_status not in allowed: return Response({"detail": "Unsupported status."}, status=400)
        if new_status in {Ticket.Status.RESOLVED, Ticket.Status.CLOSED} and not (resolution or ticket.resolution): return Response({"detail": "A resolution is required before resolving or closing."}, status=400)
        if new_status == Ticket.Status.CLOSED and ticket.status != Ticket.Status.RESOLVED: return Response({"detail": "Ticket must be resolved before closure."}, status=400)
        old = ticket.status; ticket.status = new_status
        if resolution: ticket.resolution = resolution
        if new_status == Ticket.Status.RESOLVED and not ticket.resolved_at: ticket.resolved_at = timezone.now()
        if new_status == Ticket.Status.CLOSED: ticket.closed_at = timezone.now()
        ticket.save(); activity(ticket, request.user, "STATUS_CHANGED", previous=old, current=new_status)
        notify(ticket.requester, ticket, "TICKET_STATUS", f"{ticket.reference} is now {ticket.get_status_display()}.")
        return Response(TicketDetailSerializer(ticket, context={"request": request}).data)

    @action(detail=True, methods=["post"])
    def override_priority(self, request, pk=None):
        if not is_support(request.user): return Response({"detail": "Support role required."}, status=403)
        ticket = self.get_object(); new = request.data.get("priority"); reason = request.data.get("reason", "").strip()
        if new not in Ticket.Priority.values or not reason: return Response({"detail": "Valid priority and reason are required."}, status=400)
        old = ticket.priority; ticket.priority = new; ticket.priority_override_reason = reason; ticket.save()
        activity(ticket, request.user, "PRIORITY_OVERRIDDEN", previous=old, current=new, reason=reason)
        return Response(TicketDetailSerializer(ticket, context={"request": request}).data)

    @action(detail=True, methods=["post"])
    def notes(self, request, pk=None):
        if not is_support(request.user): return Response({"detail": "Support role required."}, status=403)
        ticket = self.get_object(); serializer = WorkNoteSerializer(data=request.data); serializer.is_valid(raise_exception=True)
        note = serializer.save(ticket=ticket, author=request.user); activity(ticket, request.user, "WORK_NOTE_ADDED", internal=note.is_internal)
        return Response(WorkNoteSerializer(note).data, status=201)

    @action(detail=True, methods=["post"])
    def escalate(self, request, pk=None):
        if not is_support(request.user): return Response({"detail": "Support role required."}, status=403)
        ticket = self.get_object()
        supervisor = User.objects.filter(is_active=True, profile__role=Role.SUPERVISOR).select_related("profile").first()
        if not supervisor:
            return Response({"detail": "No active Technical Supervisor is available to receive the escalation."}, status=400)
        escalation_data = request.data.copy()
        escalation_data["internal_owner"] = supervisor.id
        serializer = EscalationSerializer(data=escalation_data); serializer.is_valid(raise_exception=True)
        escalation = serializer.save(ticket=ticket, created_by=request.user); ticket.status = Ticket.Status.ESCALATED; ticket.save()
        activity(ticket, request.user, "ESCALATED", escalation=escalation.id, supervisor=supervisor.id)
        notify(supervisor, ticket, "TICKET_ESCALATED", f"{ticket.reference} was escalated to you by {request.user.get_full_name() or request.user.username}.")
        notify(ticket.requester, ticket, "TICKET_ESCALATED", f"{ticket.reference} requires additional assistance.")
        return Response(EscalationSerializer(escalation).data, status=201)

    @action(detail=True, methods=["post"])
    def request_reopening(self, request, pk=None):
        ticket = self.get_object()
        if ticket.requester != request.user or ticket.status != Ticket.Status.CLOSED: return Response({"detail": "Only the requester can reopen a closed ticket."}, status=403)
        reason = request.data.get("reason", "").strip()
        if not reason: return Response({"detail": "A reopening reason is required."}, status=400)
        reopening = ReopeningRequest.objects.create(ticket=ticket, requester=request.user, reason=reason); ticket.status = Ticket.Status.REOPENING_REQUESTED; ticket.save()
        activity(ticket, request.user, "REOPENING_REQUESTED", request_id=reopening.id); notify(ticket.assignee, ticket, "REOPENING_REQUESTED", f"Reopening requested for {ticket.reference}.")
        return Response({"id": reopening.id}, status=201)


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    def get_queryset(self): return Notification.objects.filter(recipient=self.request.user).select_related("ticket")
    @action(detail=True, methods=["post"])
    def read(self, request, pk=None):
        notification = self.get_object(); notification.is_read = True; notification.save(update_fields=["is_read"])
        return Response({"status": "read"})


@api_view(["GET"])
def report_summary(request):
    if not is_support(request.user) and role_of(request.user) != Role.REPORT_VIEWER: return Response({"detail": "Reporting role required."}, status=403)
    qs = Ticket.objects.all()
    return Response({"total": qs.count(), "by_status": list(qs.values("status").annotate(count=Count("id")).order_by("status")), "by_priority": list(qs.values("priority").annotate(count=Count("id")).order_by("priority")), "by_assignee": list(qs.values("assignee__username").annotate(count=Count("id")).order_by("assignee__username"))})
