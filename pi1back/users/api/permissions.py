from rest_framework import permissions

class DefaultPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return request.user.is_authenticated