from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.utils.translation import gettext as _
from django.contrib import messages


class ActiveUserRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated, active, and optionally a staff member."""

    require_staff = False

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_active:
            logout(request)
            messages.error(request, _("Please log in to access this page."))
            return redirect("auth:login")

        if self.require_staff and not request.user.is_staff:
            logout(request)
            messages.error(
                request,
                _(
                    "You do not have permission to access this page. Please contact your administrator."
                ),
            )
            return redirect("auth:login")

        return super().dispatch(request, *args, **kwargs)
