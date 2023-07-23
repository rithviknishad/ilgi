from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            # admin can do anything
            return True

        if request.method in permissions.SAFE_METHODS and request.user == obj:
            # users can get their own data
            return True

        return False

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            # no access for anonymous users
            return False

        if request.user.is_superuser:
            # admins can do anything
            return True

        # regular users can only retrieve themselves
        # this is checked by UserPermission.has_object_permission()
        return view.action == "retrieve"
