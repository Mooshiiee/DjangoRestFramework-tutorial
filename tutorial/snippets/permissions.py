from rest_framework import permissions

#Custom permission to only allow owners of a snippet to edit it
class IsOwnerOrReadOnly(permissions.BasePermission):
    
    #has_objects_permission returns True if permission granted, False otherwise
    def has_object_permission(self, request, view, obj):
        #Read permissions aer allowed to any request,
        #so we will allow GET, HEAD, OPTIONS immedietly requests
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #write permissions are only allowed to the owner of the snippet
        return obj.owner == request.user
    
