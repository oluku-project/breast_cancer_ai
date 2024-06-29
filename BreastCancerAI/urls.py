from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("patients.urls")),
    path("auth/", include("accounts.urls")),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
]