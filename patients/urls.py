from django.urls import path
from .views import *


urlpatterns = [
    path("", homeview, name="home"),
    path("questionnaire/", questionnaier, name="questionnaire"),
    path("questionnaire/update/<int:pk>/", questionnaier, name="update_questionnaire"),
    path("pending/results/", pending_result, name="pending_results"),
    path(
        "delete/pending-results/", pending_result_delete, name="delete_pending_result"
    ),
    path("summary/<pk>/", summary_view, name="summary"),
    path("result/<pk>/", results, name="result"),
    path("result-hostores/", result_hostores, name="result_hostores"),
    path("delete-result/", resultdelete_view, name="delete_result"),
    path("detailed/result/<pk>/", results, name="detailed_result"),
    path("report/download/", pdfreportdownload, name="report_download"),
    path("report/print/", pdfreportprint, name="report_print"),
    path("feedback/", feedback, name="feedback"),
    path("contact/", contactview, name="contact"),
    path("about/", about, name="about"),
    path("faqs", faqs, name="faqs"),
]
