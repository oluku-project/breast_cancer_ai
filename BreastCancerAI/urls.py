from django.contrib import admin
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("patients.urls")),
    path("auth/", include("accounts.urls")),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("activate/<uidb64>/<token>/", activate, name="activate"),
    path("about/", about, name="about"),
    path("faqs", faqs, name="faqs"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
