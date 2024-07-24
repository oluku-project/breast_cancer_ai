from django.contrib import admin

from patients.models import QuestionnaireResponse, Response

# Register your models here.
admin.site.register(QuestionnaireResponse)
admin.site.register(Response)
