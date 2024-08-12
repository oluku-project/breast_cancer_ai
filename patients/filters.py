import datetime
import django_filters
from django import forms
from .models import STATE, Contact, PredictionResult
from django.db.models import F, ExpressionWrapper, DurationField, IntegerField
from django.db.models.functions import Now


class DateInput(forms.DateInput):
    input_type = "date"


class PredictionResultFilter(django_filters.FilterSet):
    # User field
    user = django_filters.CharFilter(
        field_name="user__username",
        lookup_expr="icontains",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search by Username"}
        ),
    )

    # Risk Level field
    risk_level = django_filters.CharFilter(
        field_name="risk_level",
        lookup_expr="icontains",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search by Risk Level"}
        ),
    )

    # Risk Score Min field
    risk_score_min = django_filters.NumberFilter(
        field_name="risk_score",
        lookup_expr="gte",
        label="Min Risk Score",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Min Risk Score"}
        ),
    )

    # Risk Score Max field
    risk_score_max = django_filters.NumberFilter(
        field_name="risk_score",
        lookup_expr="lte",
        label="Max Risk Score",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Max Risk Score"}
        ),
    )

    # Probability Benign Min field
    probability_benign_min = django_filters.NumberFilter(
        field_name="probability_benign",
        lookup_expr="gte",
        label="Min Probability Benign",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Min Probability Benign"}
        ),
    )

    # Probability Benign Max field
    probability_benign_max = django_filters.NumberFilter(
        field_name="probability_benign",
        lookup_expr="lte",
        label="Max Probability Benign",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Max Probability Benign"}
        ),
    )

    # Probability Malignant Min field
    probability_malignant_min = django_filters.NumberFilter(
        field_name="probability_malignant",
        lookup_expr="gte",
        label="Min Probability Malignant",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Min Probability Malignant"}
        ),
    )

    # Probability Malignant Max field
    probability_malignant_max = django_filters.NumberFilter(
        field_name="probability_malignant",
        lookup_expr="lte",
        label="Max Probability Malignant",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Max Probability Malignant"}
        ),
    )

    # Submission Date Start field
    submission_date_start = django_filters.DateFilter(
        field_name="submission_date",
        lookup_expr="gte",
        label="Submission Date Start",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Submission Date Start"}
        ),
    )

    # Submission Date End field
    submission_date_end = django_filters.DateFilter(
        field_name="submission_date",
        lookup_expr="lte",
        label="Submission Date End",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Submission Date End"}
        ),
    )

    # Date of Birth Start field
    dob_start = django_filters.DateFilter(
        field_name="dob",
        lookup_expr="gte",
        label="Date of Birth Start",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Date of Birth Start"}
        ),
    )

    # Date of Birth End field
    dob_end = django_filters.DateFilter(
        field_name="dob",
        lookup_expr="lte",
        label="Date of Birth End",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Date of Birth End"}
        ),
    )

    # Age Min field
    min_age = django_filters.NumberFilter(
        method="filter_min_age",
        label="Min Age",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Min Age"}
        ),
    )

    # Age Max field
    max_age = django_filters.NumberFilter(
        method="filter_max_age",
        label="Max Age",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Max Age"}
        ),
    )

    def filter_min_age(self, queryset, name, value):
        now = datetime.datetime.now()
        min_dob = now - datetime.timedelta(days=int(value) * 365.25)
        return queryset.filter(dob__lte=min_dob)

    def filter_max_age(self, queryset, name, value):
        now = datetime.datetime.now()
        max_dob = now - datetime.timedelta(days=int(value) * 365.25)
        return queryset.filter(dob__gte=max_dob)

    class Meta:
        model = PredictionResult
        fields = [
            "user",
            "risk_level",
            "risk_score_min",
            "risk_score_max",
            "probability_benign_min",
            "probability_benign_max",
            "probability_malignant_min",
            "probability_malignant_max",
            "submission_date_start",
            "submission_date_end",
            "dob_start",
            "dob_end",
            "min_age",
            "max_age",
        ]


class QuestionnaireResponseFilter(django_filters.FilterSet):
    # Progress Min field
    progress_min = django_filters.NumberFilter(
        field_name="progress",
        lookup_expr="gte",
        label="Min Progress Score",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Min Progress Score"}
        ),
    )

    # Progress Score Max field
    progress_max = django_filters.NumberFilter(
        field_name="progress",
        lookup_expr="lte",
        label="Max Progress Score",
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Max Progress Score"}
        ),
    )

    # Submission Date Start field
    submission_date_start = django_filters.DateFilter(
        field_name="submission_date",
        lookup_expr="gte",
        label="Submission Date Start",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Submission Date Start"}
        ),
    )

    # Submission Date End field
    submission_date_end = django_filters.DateFilter(
        field_name="submission_date",
        lookup_expr="lte",
        label="Submission Date End",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Submission Date End"}
        ),
    )
    # Updated Date Start field
    updated_date_start = django_filters.DateFilter(
        field_name="updated_date",
        lookup_expr="gte",
        label="Updated Date Start",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Updated Date Start"}
        ),
    )

    # Updated Date End field
    updated_date_end = django_filters.DateFilter(
        field_name="updated_date",
        lookup_expr="lte",
        label="Updated Date End",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Updated Date End"}
        ),
    )
    state = django_filters.ChoiceFilter(
        field_name="state",
        label="State",
        choices=STATE.choices,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    class Meta:
        model = PredictionResult
        fields = [
            "progress_min",
            "progress_max",
            "submission_date_start",
            "submission_date_end",
            "updated_date_start",
            "updated_date_end",
            "state",
        ]


class ContactFilter(django_filters.FilterSet):
    user = django_filters.CharFilter(
        field_name="user__username",
        lookup_expr="icontains",
        label="User",
        widget=forms.TextInput(attrs={"placeholder": "Search by Username"}),
    )
    name = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Name",
        widget=forms.TextInput(attrs={"placeholder": "Search by Name"}),
    )
    subject = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Subject",
        widget=forms.TextInput(attrs={"placeholder": "Search by Subject"}),
    )
    email = django_filters.CharFilter(
        lookup_expr="icontains",
        label="Email",
        widget=forms.EmailInput(attrs={"placeholder": "Search by Email"}),
    )
    # Submission Date Start field
    submission_date_start = django_filters.DateFilter(
        field_name="submission_date",
        lookup_expr="gte",
        label="Submission Date Start",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Submission Date Start"}
        ),
    )

    # Submission Date End field
    submission_date_end = django_filters.DateFilter(
        field_name="submission_date",
        lookup_expr="lte",
        label="Submission Date End",
        widget=DateInput(
            attrs={"class": "form-control", "placeholder": "Submission Date End"}
        ),
    )

    class Meta:
        model = Contact
        fields = [
            "user",
            "name",
            "subject",
            "email",
            "submission_date_start",
            "submission_date_end",
        ]
