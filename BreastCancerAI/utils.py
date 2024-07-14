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

    def compose_email(self, request, user, **kwargs):
        current_site = get_current_site(request)
        mail_subject = kwargs.get("mail_subject", "Default Subject")
        mail_temp = kwargs.get("mail_temp", "")

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
