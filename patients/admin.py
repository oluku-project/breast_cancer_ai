from django.contrib import admin

from patients.models import *

# Register your models here.
admin.site.register(QuestionnaireResponse)
admin.site.register(Response)


class PredictionResultAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "risk_level",
        "risk_score",
        "probability_benign",
        "probability_malignant",
        "submission_date",
        "dob",
        "deleted",
    )
    list_filter = ("deleted",)
    actions = ["delete_selected", "restore_selected"]

    def get_queryset(self, request):
        # Override the queryset to include deleted objects for superusers and staff
        return PredictionResult.objects.for_user(request.user)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser and not request.user.is_staff:
            if "delete_selected" in actions:
                del actions["delete_selected"]
        return actions

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser or request.user.is_staff

    def delete_selected(self, request, queryset):
        # Custom delete action to set deleted=True instead of actual deletion
        queryset.update(deleted=True)

    delete_selected.short_description = "Mark selected as deleted"

    def restore_selected(self, request, queryset):
        # Custom action to restore deleted objects
        queryset.update(deleted=False)

    restore_selected.short_description = "Restore selected deleted objects"


admin.site.register(PredictionResult, PredictionResultAdmin)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("user", "rating", "submitted_at")
    search_fields = ("user", "rating", "message")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "submitted_at")
    search_fields = ("name", "email", "message")
