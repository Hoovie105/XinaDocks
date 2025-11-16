from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    ReadOnly GLOBAL
    Write permissions MUST BE OWNER
    
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return getattr(obj, 'created_by', None) == request.user
