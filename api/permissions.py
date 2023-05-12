from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    '''Permission class restricting edit of data for non-author users.'''

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

class GroupOwnerOrReadOnly(AuthorOrReadOnly):
    '''Permission for followers to modify their subscriptions.'''

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.created_by == request.user
        )
