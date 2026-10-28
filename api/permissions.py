

from rest_framework.permissions import BasePermission


class OwnerOnly(BasePermission):

    def has_object_permission(self, request, view, obj): # if we want to set custom permission in view level use has permission and if we want to set custom permissions in object level use has object permission

        return request.user==obj.owner