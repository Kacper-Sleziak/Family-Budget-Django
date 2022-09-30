from rest_framework import permissions


class ListCreatorPermission(permissions.BasePermission):
    """
    Return true if user is creator of List
    """

    message = "Only Creator can do this operations!"

    def has_object_permission(self, request, view, obj):
        return obj.is_creator(request.user)


class ListParticipantPermission(permissions.BasePermission):
    """
    Return true if user is one of the participants in given List
    """

    message = "You dont't have access to this list!"

    def has_object_permission(self, request, view, obj):
        return obj.has_access(request.user)
