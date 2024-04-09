from rest_framework import permissions


class OwnerAuthenticated(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return self.has_permission(request,
                                   view) and request.user == obj.user  # kiểm tra xem user hiện tại có phải là chủ sở hữu của đối tượng obj.user không
