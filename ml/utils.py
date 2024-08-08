from django.shortcuts import get_object_or_404
from accounts.models import Account
from ml.models import ActivityLog


def log_user_activity(request,user, action):

    # user = get_object_or_404(Account, pk=user.pk)
    if isinstance(user,Account):
        ActivityLog.objects.create(
            user=user,
            action=action,
            ip_address=request.META.get("REMOTE_ADDR"),
            user_agent=request.META.get("HTTP_USER_AGENT"),
        )
    