from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Role(models.TextChoices):
    EMPLOYEE = "EMPLOYEE", "Employee"
    TECHNICIAN = "TECHNICIAN", "Support Technician"
    SUPERVISOR = "SUPERVISOR", "Technical Supervisor"
    ADMIN = "ADMIN", "System Administrator"
    REPORT_VIEWER = "REPORT_VIEWER", "Report Viewer"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.EMPLOYEE)

    def __str__(self):
        return f"{self.user.get_username()} ({self.get_role_display()})"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Ticket(models.Model):
    class Status(models.TextChoices):
        SUBMITTED = "SUBMITTED", "Submitted"
        OPEN = "OPEN", "Open"
        ASSIGNED = "ASSIGNED", "Assigned"
        IN_PROGRESS = "IN_PROGRESS", "In Progress"
        WAITING = "WAITING", "Waiting for Information"
        ESCALATED = "ESCALATED", "Escalated"
        RESOLVED = "RESOLVED", "Resolved"
        CLOSED = "CLOSED", "Closed"
        REOPENING_REQUESTED = "REOPENING_REQUESTED", "Reopening Requested"

    class Impact(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    class Urgency(models.TextChoices):
        LOW = "LOW", "Low"
        MEDIUM = "MEDIUM", "Medium"
        HIGH = "HIGH", "High"

    class Priority(models.TextChoices):
        LOW = "LOW", "Low"
        NORMAL = "NORMAL", "Normal"
        HIGH = "HIGH", "High"
        CRITICAL = "CRITICAL", "Critical"

    reference = models.CharField(max_length=24, unique=True, editable=False)
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="requested_tickets")
    requester_position = models.CharField(max_length=120)
    requester_department = models.CharField(max_length=120)
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_tickets")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="tickets")
    title = models.CharField(max_length=160)
    description = models.TextField()
    impact = models.CharField(max_length=10, choices=Impact.choices, default=Impact.MEDIUM)
    urgency = models.CharField(max_length=10, choices=Urgency.choices, default=Urgency.MEDIUM)
    priority = models.CharField(max_length=10, choices=Priority.choices, default=Priority.NORMAL)
    status = models.CharField(max_length=24, choices=Status.choices, default=Status.SUBMITTED)
    priority_override_reason = models.TextField(blank=True)
    resolution = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["status", "priority"]), models.Index(fields=["requester", "created_at"]), models.Index(fields=["assignee", "status"])]

    @staticmethod
    def suggested_priority(impact, urgency):
        if impact == Ticket.Impact.HIGH and urgency == Ticket.Urgency.HIGH:
            return Ticket.Priority.CRITICAL
        if impact == Ticket.Impact.HIGH or urgency == Ticket.Urgency.HIGH:
            return Ticket.Priority.HIGH
        if impact == Ticket.Impact.LOW and urgency == Ticket.Urgency.LOW:
            return Ticket.Priority.LOW
        return Ticket.Priority.NORMAL

    def save(self, *args, **kwargs):
        if not self.reference:
            stamp = timezone.now().strftime("%Y%m%d")
            sequence = Ticket.objects.filter(reference__startswith=f"TSMS-{stamp}-").count() + 1
            self.reference = f"TSMS-{stamp}-{sequence:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.reference


class TicketActivity(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="activities")
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)
    event_type = models.CharField(max_length=60)
    details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]


class WorkNote(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="work_notes")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    body = models.TextField()
    is_internal = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]


class Escalation(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="escalations")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="created_escalations")
    internal_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="owned_escalations")
    reason = models.TextField()
    assistance_requested = models.TextField()
    follow_up = models.TextField(blank=True)
    outcome = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ReopeningRequest(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="reopening_requests")
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    reason = models.TextField()
    reviewed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True, related_name="reviewed_reopening_requests")
    outcome = models.CharField(max_length=20, choices=[("PENDING", "Pending"), ("REOPENED", "Reopened"), ("DECLINED", "Declined")], default="PENDING")
    review_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)


class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, null=True, blank=True, related_name="notifications")
    event = models.CharField(max_length=80)
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
