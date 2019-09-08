from rest_framework.permissions import (
    BasePermission,
    SAFE_METHODS,
    IsAdminUser)


class IsAuthorOrAdmin(BasePermission):
    message = 'You must be the Auther or Admin of this object.'
    # my_safe_method=['GET','PUT']
    def has_object_permission(self, request, view, obj):
        #member = Membership.objects.get(user=request.user)
        #member.is_active
        return obj.author == request.user