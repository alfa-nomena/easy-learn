from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, *args, **kwargs):
        return bool(
            request.method in (permissions.SAFE_METHODS + ("POST",)) 
            or (request.user and request.user.is_authenticated)
        )