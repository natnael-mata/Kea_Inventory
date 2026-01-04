from rest_framework import permissions
from .models import UserRole

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return UserRole.objects.filter(username=request.user, role_name='Admin').exists() or request.user.is_superuser

class IsSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return UserRole.objects.filter(username=request.user, role_name='Supervisor').exists()

class IsStoreKeeper(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return UserRole.objects.filter(username=request.user, role_name='Store Keeper').exists()

class IsAdminOrStoreKeeper(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return UserRole.objects.filter(username=request.user, role_name__in=['Admin', 'Store Keeper']).exists() or request.user.is_superuser

class IsAdminOrSupervisorOrStoreKeeper(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return UserRole.objects.filter(username=request.user, role_name__in=['Admin', 'Supervisor', 'Store Keeper']).exists() or request.user.is_superuser
