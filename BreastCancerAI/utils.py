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


class MailUtils:
    def compose_email(self, request, user):
        current_site = get_current_site(request)
        mail_subject = "Reset Your Password"
        message_html = render_to_string(
            "accounts/reset_password_email.html",
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
