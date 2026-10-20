from django.contrib import admin
from .models import Category, Escalation, Notification, ReopeningRequest, Ticket, TicketActivity, UserProfile, WorkNote

admin.site.register([Category, Ticket, TicketActivity, WorkNote, Escalation, ReopeningRequest, Notification, UserProfile])
