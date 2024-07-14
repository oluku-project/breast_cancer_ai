from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetConfirmView,
    PasswordResetConfirmView as AuthPasswordResetConfirmView,
)
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import CreateView, View, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from BreastCancerAI.mixins import CustomPermissionMixin
from BreastCancerAI.utils import MailUtils
from .forms import LoginForm, RegistrationForm, SetPasswordForm
from .models import Account
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator


class UserRegistrationView(MailUtils, CreateView):
    form_class = RegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("auth:login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user.username = str(email.split("@")[0])
        user.password = make_password(password)
        user.save()

        group, created = Group.objects.get_or_create(name="Users")
        if created:
            group.save()

        user.groups.add(group)

        # Send activation email
        mail_temp = "accounts/account_verification_email.html"
        mail_subject = "Activate Your Account"
        self.compose_email(
            self.request, user, mail_subject=mail_subject, mail_temp=mail_temp
        )

        self.request.session["registration_success"] = True

        return redirect(self.success_url)

    def form_invalid(self, form):

        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, _(f"{field}: {error}"))
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = _("Sign Up")
        return context


userregistrationview = UserRegistrationView.as_view()


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(Account, pk=uid)
        except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
            user = None

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, _("Congratulations! Your account is activated."))
            return redirect("auth:login")
        else:
            messages.error(request, _("Invalid activation link"))
            return redirect("auth:register")


activateaccountview = ActivateAccountView.as_view()


class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("auth:user_dashboard")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = auth.authenticate(email=username, password=password)
        if user is not None:
            auth.login(self.request, user)
            messages.success(self.request, _("You are now logged in."))
            return super().form_valid(form)
        else:
            messages.error(self.request, _("Invalid login credentials."))
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, _("Invalid form submission."))
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = "Log In"
        return context


loginview = LoginView.as_view()


class LogoutView(CustomPermissionMixin, View):
    def get(self, request):
        auth.logout(request)
        messages.success(request, _("You are logged out."))
        return redirect("auth:login")


logoutview = LogoutView.as_view()


class ForgotPasswordView(MailUtils, View):
    template_name = "accounts/forgotPassword.html"

    def get(self, request):
        return render(request, self.template_name, {"title_root": "Forgot Password"})

    def post(self, request):
        email = request.POST.get("email")
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)
            mail_temp = "accounts/reset_password_email.html"
            mail_subject = "Reset Your Password"
            self.compose_email(
                self.request, user, mail_subject=mail_subject, mail_temp=mail_temp
            )
            messages.success(
                request, _("Password reset email has been sent to your email address.")
            )
            return redirect("auth:login")
        else:
            messages.error(request, _("Account does not exist!"))
            return redirect("auth:forgotPassword")


forgotpasswordview = ForgotPasswordView.as_view()


class PasswordResetConfirmView(AuthPasswordResetConfirmView):
    form_class = SetPasswordForm
    template_name = "accounts/password_reset_confirm.html"
    success_url = reverse_lazy("auth:password_reset_complete")

    def form_valid(self, form):
        user = form.save()
        messages.success(
            self.request,
            _(
                "Your password has been reset successfully. You can now log in with your new password."
            ),
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(self.request, f"{field}: {error}")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = _("Reset Password")
        return context


passwordresetconfirmview = PasswordResetConfirmView.as_view()


class PasswordResetCompleteView(TemplateView):
    template_name = "accounts/password_reset_complete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = _("Password Reset Complete - Breast Cancer Prediction")
        return context


passwordresetcompleteview = PasswordResetCompleteView.as_view()


class PrivacyView(TemplateView):
    template_name = "accounts/privacy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = _("Privacy")
        return context


privacyview = PrivacyView.as_view()


class TermsView(TemplateView):
    template_name = "accounts/terms.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = _("Terms")
        return context


termsview = TermsView.as_view()


class UserDashboardView(TemplateView):
    template_name = "accounts/user-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = _("User Dashboard")
        return context


userdashboardview = UserDashboardView.as_view()
