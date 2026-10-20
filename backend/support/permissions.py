from rest_framework.permissions import BasePermission
from .models import Role


SUPPORT_ROLES = {Role.TECHNICIAN, Role.SUPERVISOR, Role.ADMIN}


def role_of(user):
    return getattr(getattr(user, "profile", None), "role", Role.EMPLOYEE)


def is_support(user):
    return role_of(user) in SUPPORT_ROLES


class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return role_of(request.user) == Role.ADMIN or request.user.is_superuser


class IsSupportUser(BasePermission):
    def has_permission(self, request, view):
        return is_support(request.user)
