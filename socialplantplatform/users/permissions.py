from rest_framework.permissions import BasePermission, SAFE_METHODS


class UserPermission(BasePermission):

    # def has_permission(self, request, view):
    #     return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, user):
        return request.user == user

