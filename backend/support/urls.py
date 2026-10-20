from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, NotificationViewSet, TicketViewSet, login_view, logout_view, me_view, report_summary, support_users_view

router = DefaultRouter()
router.register("tickets", TicketViewSet, basename="ticket")
router.register("categories", CategoryViewSet, basename="category")
router.register("notifications", NotificationViewSet, basename="notification")

urlpatterns = [
    path("auth/login/", login_view), path("auth/logout/", logout_view), path("auth/me/", me_view), path("users/support/", support_users_view),
    path("reports/summary/", report_summary), path("", include(router.urls)),
]
