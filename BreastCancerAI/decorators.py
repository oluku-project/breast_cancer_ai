from django.conf import settings
from functools import wraps
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from django.http import JsonResponse

from django.core.exceptions import ImproperlyConfigured


def no_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        if response.status_code == 302 and response.url == settings.LOGIN_URL:
            response.status_code = 200
        return response

    return _wrapped_view


def login_not_required(view_func):
    """
    Decorator that marks a view as not requiring login.
    """

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is already authenticated, proceed with the view as usual
            return view_func(request, *args, **kwargs)
        else:
            # If the user is not authenticated, check if a redirect to the login page is needed
            response = view_func(request, *args, **kwargs)
            if (
                isinstance(response, HttpResponseRedirect)
                and response.url == settings.LOGIN_URL
            ):
                # If the response is a redirect to the login page, change it to a regular response
                response.status_code = 200  # Change status code to prevent redirection
            return response

    return _wrapped_view


def check_permissions(user, permissions, check_staff=False):
    """
    Check if user type, is_active, is_staff (optional), and permissions are valid.
    """
    if not user.is_active:
        return False, "Your account is inactive. Please contact support."

    if check_staff and not user.is_staff:
        return False, "You do not have staff privileges to access this page."

    group = user.groups.first()

    if permissions and group:
        # Check if all required permissions exist in the group's permissions
        required_permission_set = set(permissions)
        group_permission_set = set(group.permissions.values_list("codename", flat=True))
        if not required_permission_set.issubset(group_permission_set):
            return False, "You do not have permission to access this page."

    return True, None


def logout_and_response(request, isjson):
    """
    Logout user and return appropriate JSON response or redirect.
    """
    from accounts.views import logoutview

    # call logout here
    response = logoutview(request)

    if isjson:
        response_data = {"success": False, "redirect_url": reverse_lazy("login")}
        return JsonResponse(response_data)
    else:
        return response


def custom_permission_required(
    permissions=None, message=None, isjson=False, check_staff=False
):
    """
    Decorator for function-based views to check user types and permissions.
    """

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            user = request.user
            if user.is_authenticated and request.session.session_key is not None:
                valid, msg = check_permissions(user, permissions, check_staff)
                if not valid:
                    messages.error(request, msg)
                    return logout_and_response(request, isjson)
            else:
                messages.error(request, "Please log in to access this page.")
                return logout_and_response(request, isjson)
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


# @custom_permission_required(user_types=["superadmin"], permissions=["view_data"], isjson=True)
