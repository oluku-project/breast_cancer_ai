from django.urls import path
from .views import (
    userregistrationview,
    loginview,
    activateaccountview,
    forgotpasswordview,
    passwordresetconfirmview,
    passwordresetcompleteview,
    privacyview,
    termsview,
    userdashboardview,
)

app_name = "auth"
urlpatterns = [
    path("signup/", userregistrationview, name="signup"),
    path("login/", loginview, name="login"),
    path("activate/<uidb64>/<token>/", activateaccountview, name="activate"),
    path("forgot-password/", forgotpasswordview, name="forgotPassword"),
    path(
        "reset-password/<uidb64>/<token>/",
        passwordresetconfirmview,
        name="password_reset_confirm",
    ),
    path(
        "reset-password-complete/",
        passwordresetcompleteview,
        name="password_reset_complete",
    ),
    path("privacy/", privacyview, name="privacy"),
    path("terms/", termsview, name="terms"),
    path("user/dashboard", userdashboardview, name="user_dashboard"),
]
