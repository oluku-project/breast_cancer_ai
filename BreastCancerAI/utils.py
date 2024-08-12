from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives


class UserTypes:
    USER_GROUP = "Users"
    DOCTOR_GROUP = "Professional Doctors"
MONTHS = [
    (1, "January"),
    (2, "February"),
    (3, "March"),
    (4, "April"),
    (5, "May"),
    (6, "June"),
    (7, "July"),
    (8, "August"),
    (9, "September"),
    (10, "October"),
    (11, "November"),
    (12, "December"),
]

PASSWORD_VALIDITY = [
    {
        "title": "Step One",
        "des": "Your password can’t be too similar to your other personal information.",
        "css": "text-muted text-warning",
        "txt": "text-warning",
    },
    {
        "title": "Step Two",
        "des": "Your password must contain at least 8 characters.",
        "css": "text-success",
        "txt": "text-success",
    },
    {
        "title": "Step Three",
        "des": "Your password can’t be a commonly used password.",
        "css": "text-muted text-danger",
        "txt": "text-danger",
    },
    {
        "title": "Step Four",
        "des": "Your password can’t be entirely numeric.",
        "css": "text-primary",
        "txt": "text-primary",
    },
]


class MailUtils:

    def compose_email(self, request, user, **kwargs):
        """Instance method to send an email."""
        self._compose_email(request, user, **kwargs)

    @staticmethod
    def send_activation_email(request, user, **kwargs):
        """Static method to send an email."""
        MailUtils._compose_email(request, user, **kwargs)

    @staticmethod
    def _compose_email(request, user, **kwargs):
        """Private method to handle email composition and sending."""
        current_site = get_current_site(request)
        mail_subject = kwargs.get("mail_subject", "Activate Your Account")
        mail_temp = kwargs.get("mail_temp", "accounts/account_verification_email.html")

        message_html = render_to_string(
            mail_temp,
            {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": default_token_generator.make_token(user),
            },
        )

        message_plain = strip_tags(message_html)
        to_email = user.email

        email = EmailMultiAlternatives(mail_subject, message_plain, to=[to_email])
        email.attach_alternative(message_html, "text/html")
        email.send()
