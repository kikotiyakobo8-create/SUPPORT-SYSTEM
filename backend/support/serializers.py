from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category, Escalation, Notification, ReopeningRequest, Role, Ticket, TicketActivity, UserProfile, WorkNote


class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="profile.role", read_only=True)
    display_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "display_name", "role"]
    def get_display_name(self, obj):
        return obj.get_full_name() or obj.username


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "description", "is_active"]


class ActivitySerializer(serializers.ModelSerializer):
    actor = UserSerializer(read_only=True)
    class Meta:
        model = TicketActivity
        fields = ["id", "event_type", "details", "actor", "created_at"]


class WorkNoteSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = WorkNote
        fields = ["id", "body", "is_internal", "author", "created_at"]
        read_only_fields = ["author"]


class EscalationSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    internal_owner_detail = UserSerializer(source="internal_owner", read_only=True)
    class Meta:
        model = Escalation
        fields = ["id", "reason", "assistance_requested", "internal_owner", "internal_owner_detail", "follow_up", "outcome", "created_by", "created_at", "updated_at"]
        read_only_fields = ["created_by"]


class ReopeningRequestSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    reviewed_by = UserSerializer(read_only=True)
    class Meta:
        model = ReopeningRequest
        fields = ["id", "reason", "requester", "outcome", "review_note", "reviewed_by", "created_at", "reviewed_at"]
        read_only_fields = ["requester", "outcome", "review_note", "reviewed_by", "created_at", "reviewed_at"]


class TicketListSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    assignee = UserSerializer(read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Ticket
        fields = ["id", "reference", "title", "category", "category_name", "requester", "assignee", "priority", "status", "created_at", "updated_at"]


class TicketDetailSerializer(TicketListSerializer):
    activities = ActivitySerializer(many=True, read_only=True)
    work_notes = serializers.SerializerMethodField()
    escalations = EscalationSerializer(many=True, read_only=True)
    reopening_requests = ReopeningRequestSerializer(many=True, read_only=True)
    class Meta(TicketListSerializer.Meta):
        fields = TicketListSerializer.Meta.fields + ["description", "requester_position", "requester_department", "impact", "urgency", "priority_override_reason", "resolution", "resolved_at", "closed_at", "activities", "work_notes", "escalations", "reopening_requests"]
    def get_work_notes(self, obj):
        notes = obj.work_notes.all()
        role = getattr(self.context["request"].user.profile, "role", Role.EMPLOYEE)
        if role == Role.EMPLOYEE:
            notes = notes.filter(is_internal=False)
        return WorkNoteSerializer(notes, many=True).data


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ["title", "description", "category", "requester_position", "requester_department", "impact", "urgency"]
    def create(self, validated_data):
        request = self.context["request"]
        ticket = Ticket.objects.create(requester=request.user, priority=Ticket.suggested_priority(validated_data["impact"], validated_data["urgency"]), **validated_data)
        TicketActivity.objects.create(ticket=ticket, actor=request.user, event_type="TICKET_CREATED", details={"status": ticket.status})
        return ticket


class NotificationSerializer(serializers.ModelSerializer):
    ticket_reference = serializers.CharField(source="ticket.reference", read_only=True)
    class Meta:
        model = Notification
        fields = ["id", "event", "message", "ticket", "ticket_reference", "is_read", "created_at"]
