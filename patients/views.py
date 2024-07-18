from django.urls import reverse
from django.shortcuts import render, redirect
from django.db import transaction
from patients.utils import QUESTIONS, section_headers
from django.views.generic import DetailView, View
from typing import List
from django.shortcuts import get_object_or_404
from .models import QuestionnaireResponse, Response


class QuestionnaireView(View):
    template_name = "patients/questionnaier.html"
    responseID = None

    def get(self, request, *args, **kwargs):
        self.responseID = kwargs.get("pk", None)
        return render(request, self.template_name, self.get_context())

    def post(self, request, *args, **kwargs):
        self.responseID = kwargs.get("pk", None)

        # Extract form data
        form_data = request.POST
        progress = form_data.get("progress", 0)

        # Filter out questions with "Yes" responses (where answer is "on")
        responses = {key: value for key, value in form_data.items() if value == "on"}
        if responses:
            # Save responses to the database
            response_instance, msg = self.save_responses(
                request.user,
                responses,
                progress,
            )
            # Add a success message
            messages.success(request, msg)
            return redirect(reverse("summary", kwargs={"pk": response_instance.id}))

        return render(request, self.template_name, self.get_context())

    def get_context(self):
        question_keys = (
            self.get_question_keys_for_response(self.responseID)
            if self.responseID
            else None
        )
        context = {
            "questions": QUESTIONS,
            "section_headers": section_headers,
            "question_keys": question_keys,
            "title_root": "Questionnaire",
        }
        return context

    def save_responses(self, user, responses, progress):
        # Start a transaction to ensure atomicity
        with transaction.atomic():
            # Check if responseID is provided
            if self.responseID:
                # Try to retrieve the existing QuestionnaireResponse instance
                response_instance = QuestionnaireResponse.objects.get(
                    id=self.responseID
                )

                # Delete existing responses
                response_instance.responses.all().delete()

                # Update progress if it has changed
                if response_instance.progress != progress:
                    response_instance.progress = progress
                    response_instance.save()
                    msg = "Your responses have been updated and successfully submitted."
            else:
                # Create a new QuestionnaireResponse instance
                response_instance = QuestionnaireResponse.objects.create(
                    user=user, progress=progress
                )
                msg = "Your responses have been created and successfully submitted."
            # Create new responses for the QuestionnaireResponse instance
            response_objects = [
                Response(questionnaire_response=response_instance, question_key=key)
                for key in responses.keys()
            ]
            Response.objects.bulk_create(response_objects)

        return response_instance, msg

    def get_question_keys_for_response(self, pk) -> List[str]:
        response_instance = get_object_or_404(QuestionnaireResponse, pk=pk)
        # Retrieve all related Response instances and extract question_key as a list
        question_keys = response_instance.responses.all().values_list(
            "question_key",
            flat=True,
        )
        return list(question_keys)


questionnaier = QuestionnaireView.as_view()


class SummaryView(DetailView):
    model = QuestionnaireResponse
    template_name = "patients/summary.html"
    context_object_name = "response_instance"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response_instance = self.object
        grouped_questions = {header: [] for header in section_headers}

        for response in response_instance.responses.all():
            question = next(q for q in QUESTIONS if q[1] == response.question_key)
            index = QUESTIONS.index(question) // 6
            section_header = section_headers[index]
            grouped_questions[section_header].append(question[0])

        # Remove empty groups
        grouped_questions = {k: v for k, v in grouped_questions.items() if v}
        context.update(
            {
                "grouped_questions": grouped_questions,
                "section_headers": section_headers,
            }
        )
        return context


summary_view = SummaryView.as_view()


from django.http import HttpResponse
import csv
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def admin_system_settings(request):
   
    return render(request, "admin_system_settings.html")
def admin_reports(request):
    # Logic to fetch and process report data
    reports = [
        {"id": 1, "name": "Monthly Assessment Report", "created_date": "2024-06-15"},
        {"id": 2, "name": "User Demographics Report", "created_date": "2024-06-10"},
    ]
    return render(request, "admin_reports.html", {"reports": reports})


def admin_record_management(request):
    # Logic to fetch and process record data
    records = [
        {
            "id": 1,
            "user": "John Doe",
            "questionnaire": "Breast Cancer Risk Assessment",
            "date": "2024-06-01",
            "score": 85,
            "status": "Completed",
        },
        {
            "id": 2,
            "user": "Jane Smith",
            "questionnaire": "Breast Cancer Risk Assessment",
            "date": "2024-06-05",
            "score": 78,
            "status": "Completed",
        },
        {
            "id": 3,
            "user": "Mary Johnson",
            "questionnaire": "Breast Cancer Risk Assessment",
            "date": "2024-06-10",
            "score": 92,
            "status": "Pending",
        },
    ]
    return render(request, "admin_record_management.html", {"records": records})


def admin_data_visualization(request):
    # You can add logic to fetch and process data here
    return render(request, "admin_data_visualization.html")


# @login_required
def admin_questionnaire_management(request):
    # Fetch questionnaire data from the database
    questionnaires = [
        {"id": 1, "title": "Health Risk Assessment", "description": "Assessment to determine general health risks.", "creation_date": "2024-06-01", "status": "Active"},
        {"id": 2, "title": "Breast Cancer Awareness", "description": "Questionnaire to raise awareness about breast cancer.", "creation_date": "2024-05-15", "status": "Inactive"},
        # Add more questionnaire data here
    ]
    return render(request, 'admin_questionnaire_management.html', {'questionnaires': questionnaires})

# @login_required
def admin_user_management(request):
    # Fetch user data from the database
    users = [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
            "dob": "1990-01-01",
            "gender": "Male",
            "signup_date": "2024-06-01",
            "status": "Active",
        },
        # Add more user data here
    ]
    return render(request, "admin_user_management.html", {"users": users})


# @login_required
def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def export_data(request):
    if request.method == "POST":
        export_format = request.POST.get("export_format")

        # Dummy data for export
        data = [
            {"name": "John Doe", "age": 30, "email": "john@example.com"},
            {"name": "Jane Smith", "age": 25, "email": "jane@example.com"},
        ]

        if export_format == "csv":
            response = HttpResponse(content_type="text/csv")
            response["Content-Disposition"] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            writer.writerow(["Name", "Age", "Email"])
            for row in data:
                writer.writerow([row["name"], row["age"], row["email"]])
            return response

        elif export_format == "pdf":
            # Implement PDF export logic
            pass

        elif export_format == "json":
            response = HttpResponse(content_type="application/json")
            response["Content-Disposition"] = 'attachment; filename="data.json"'
            response.write(json.dumps(data))
            return response

    return redirect("data_export_import")


def import_data(request):
    if request.method == "POST":
        import_file = request.FILES["import_file"]
        # Implement file processing logic
        pass

    return redirect("data_export_import")


def data_export_import(request):
    return render(request, "data_export_import.html")


# Create your views here.
def index(request):
    context = {"what_url": "MAIN DASHBOARD", "title_root": "Dashboard"}

    return render(request, "home.html", context)


def charts_and_data_visualization(request):
    context = {"what_url": "MAIN DASHBOARD", "title_root": "Dashboard"}
    # {% static 'images/chart-visualizing-1.jpg' %}
    return render(request, "charts_and_data_visualization.html", context)


def record_details(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Record Details - Breast Cancer Prediction",
    }
    # {% static 'images/chart-visualizing-1.jpg' %}
    return render(request, "record-details.html", context)


def about(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "About Us - Breast Cancer Prediction",
    }

    return render(request, "about.html", context)


def faqs(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "FAQS - Breast Cancer Prediction",
    }

    return render(request, "faqs.html", context)


def contacts(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Contact - Breast Cancer Prediction",
    }

    return render(request, "contacts.html", context)

def privacy(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Privacy",
    }

    return render(request, "privacy.html", context)
def terms(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Terms - Breast Cancer Prediction",
    }

    return render(request, "terms.html", context)
def profile(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Profile - Breast Cancer Prediction",
    }

    return render(request, "profile.html", context)
def auth_login(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Login - Breast Cancer Prediction",
    }

    return render(request, "auth-login.html", context)
def pwd_recovery(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Password Covery - Breast Cancer Prediction",
    }

    return render(request, "pwd-recovery.html", context)
def user_dashboard(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "User Dashboard - Breast Cancer Prediction",
    }

    return render(request, "user-dashboard.html", context)
def user_profile(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "User Profile - Breast Cancer Prediction",
    }

    return render(request, "user-profile.html", context)


def results(request):
    user = {
        "name": "Jane Doe",
        "age": 45,
        "health_history": "Family history of breast cancer",
        "symptoms": "Lump in the breast, skin changes",
    }
    risk_level = "high"  # Example risk level
    risk_score = 75  # Example risk score
    risk_factors = [
        {"question": "Lump in the breast", "value": 17.99},
        {"question": "Pain in the armpit or breast", "value": 21.25},
        {"question": "Redness of the breast skin", "value": 132.90},
        # Add more factors as needed
    ]

    context = {
        "user": user,
        "risk_level": risk_level,
        "risk_score": risk_score,
        "risk_factors": risk_factors,
        "average_risk_score": 50,
        "title_root": "Results - Breast Cancer Prediction",
    }

    return render(request, "results.html", context)


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        # Send email
        send_mail(
            f"Contact Form Submission from {name}",
            message,
            email,
            ["support@example.com"],  # Your support email
            fail_silently=False,
        )

        messages.success(request, "Your message has been sent successfully.")
        return redirect("contact")  # Redirect to the same page or a thank you page

    return render(request, "contact.html")


from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import QuestionnaireForm


class QuestionnaireView(FormView):
    template_name = "questionnaier.html"
    form_class = QuestionnaireForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        # Process form data here
        responses = form.cleaned_data
        print(responses)  # For demonstration
        return super().form_valid(form)


questionnaier = QuestionnaireView.as_view()
