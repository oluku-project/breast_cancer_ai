from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("terms/", terms, name="terms"),
    path("privacy/", privacy, name="privacy"),
    path("profile/", profile, name="profile"),
    path("results/", results, name="results"),
    path("contact/", contact, name="contact"),
    path("faqs/", faqs, name="faqs"),
    path("auth-login/", auth_login, name="auth_login"),
    path("pwd-recovery/", pwd_recovery, name="pwd_recovery"),
    path("user-dashboard/", user_dashboard, name="user_dashboard"),
    path("user-profile/", user_profile, name="user_profile"),
    path("export/", export_data, name="export_data"),
    path("import/", import_data, name="import_data"),
    path("data/", data_export_import, name="data_export_import"),
    path("admin-dashboard/", admin_dashboard, name="admin_dashboard"),
    path(
        "admin-user-management/",
        admin_user_management,
        name="admin_user_management",
    ),
    path(
        "admin-questionnaire-management/",
        admin_questionnaire_management,
        name="admin_questionnaire_management",
    ),
    path(
        "admin-data-visualization/",
        admin_data_visualization,
        name="admin_data_visualization",
    ),
    path(
        "admin-record-management/",
        admin_record_management,
        name="admin_record_management",
    ),
    path(
        "admin-system-settings/",
        admin_system_settings,
        name="admin_system_settings",
    ),
    path("admin-reports/", admin_reports, name="admin_reports"),
    path("contacts/", contacts, name="contacts"),
    path("record-details/", record_details, name="record_details"),
    path("visualization/", charts_and_data_visualization, name="visualization"),
    # Done with the below urls
    path("questionnaire/", questionnaier, name="questionnaire"),
    path("questionnaire/update/<int:pk>/", questionnaier, name="update_questionnaire"),
    path("summary/<pk>/", summary_view, name="summary"),
    path("results/<pk>/", results, name="results"),
]
