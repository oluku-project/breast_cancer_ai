from .decorators import custom_permission_required


class CustomPermissionMixin:
    """
    Custom mixin for handling class-based views
    """

    def dispatch(self, request, *args, **kwargs):
        permissions = getattr(self, "required_permissions", [])
        isjson = getattr(self, "isjson", False)
        message = getattr(self, "permission_denied_message", None)
        check_staff = getattr(self, "check_staff", False)
        user_type_decorator = custom_permission_required(
            permissions,
            message,
            isjson,
            check_staff=check_staff,
        )
        decorated = user_type_decorator(super().dispatch)
        return decorated(request, *args, **kwargs)
