from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsAuthenticatedWithMessage(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if super().has_permission(request, view):
            return True
        raise PermissionDenied(
            'You must be authenticated to perform this action.')
