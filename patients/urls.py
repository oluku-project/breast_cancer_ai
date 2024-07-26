from django.urls import path
from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("profile/", profile, name="profile"),  # done
    path("user-dashboard/", user_dashboard, name="user_dashboard"),  # done
    path("user-profile/", user_profile, name="user_profile"),  # done
    path("contact/", contact, name="contact"),
    path("faqs/", faqs, name="faqs"),
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
    path("result-hostores/", result_hostores, name="result_hostores"),
    path("visualization/", charts_and_data_visualization, name="visualization"),
    # Done with the below urls
    path("questionnaire/", questionnaier, name="questionnaire"),
    path("questionnaire/update/<int:pk>/", questionnaier, name="update_questionnaire"),
    path("pending/results/", pending_result, name="pending_results"),
    path("delete/pending-results/", pending_result_delete, name="delete_pending_result"),
    path("summary/<pk>/", summary_view, name="summary"),
    path("result/<pk>/", results, name="result"),
    path("delete-result/", resultdelete_view, name="delete_result"),
    path("detailed/result/<pk>/", results, name="detailed_result"),
]
