from django.urls import reverse
from django.shortcuts import render, redirect
from django.db import transaction
from patients.utils import QUESTIONS, HelpResponse, section_headers, RISK_LEVEL, CATEGORIES
from django.views.generic import DetailView, View
from typing import List
from django.shortcuts import get_object_or_404
from .models import STATE, PredictionResult, QuestionnaireResponse, Response
from BreastCancerAI import settings
import pandas as pd
import pickle5 as pickle
from django_filters.views import FilterView
from .filters import PredictionResultFilter, QuestionnaireResponseFilter


class QuestionnaireView(View):
    template_name = "patients/questionnaire.html"
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
                "title_root": "Summary",
            }
        )
        return context

summary_view = SummaryView.as_view()

class PredictionView(DetailView):
    model = QuestionnaireResponse
    template_name = "patients/results.html"
    context_object_name = "response_instance"

    def get_clean_data(self):
        data = pd.read_csv(f"{settings.STATICFILES_DIRS[0]}/model/data.csv")
        data = data.drop(["Unnamed: 32", "id"], axis=1)
        data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
        return data

    def get_risk_level_from_score(self, score):
        formatted_score = f"{score * 100:.2f}"
        if score < 0.33:
            risk_level = RISK_LEVEL[0]
        elif score < 0.66:
            risk_level = RISK_LEVEL[1]
        else:
            risk_level = RISK_LEVEL[2]
        description = risk_level["description"][0].format(score=formatted_score)
        return {
            "level": risk_level["level"],
            "info": risk_level["info"],
            "score": description,
            "next": risk_level["next_steps"][0]["messages"][0],
            "next_steps": risk_level["next_steps"],
            "resources": risk_level["resources"],
            "recommendations": risk_level["recommendations"],
        }

    def get_default_values(self):
        with open(
            f"{settings.STATICFILES_DIRS[0]}/model/default_values.pkl", "rb"
        ) as f:
            default_values = pickle.load(f)
        return default_values

    def add_predictions(self, input_data):
        dir = settings.STATICFILES_DIRS[0]
        model = pickle.load(open(f"{dir}/model/model.pkl", "rb"))
        scaler = pickle.load(open(f"{dir}/model/scaler.pkl", "rb"))

        input_df = pd.DataFrame([input_data])
        input_array_scaled = scaler.transform(input_df)
        prediction = model.predict(input_array_scaled)
        probabilities = model.predict_proba(input_array_scaled)
        return probabilities

    def make_prediction(self, probabilities):
        # Get the probability of the positive class (malignant)
        risk_score = probabilities[0][1]
        risk_level = self.get_risk_level_from_score(risk_score)
        return risk_level, risk_score

    def get_scaled_values(self, input_dict):
        data = self.get_clean_data()
        X = data.drop(["diagnosis"], axis=1)
        scaled_dict = {}
        for key, value in input_dict.items():
            max_val = X[key].max()
            min_val = X[key].min()
            scaled_value = (value - min_val) / (max_val - min_val)
            scaled_dict[key] = scaled_value
        return scaled_dict

    def get_line_scatter_chart(self, input_data):
        input_data = self.get_scaled_values(input_data)
        mean = [
            round(input_data["radius_mean"], 2),
            round(input_data["texture_mean"], 2),
            round(input_data["perimeter_mean"], 2),
            round(input_data["area_mean"], 2),
            round(input_data["smoothness_mean"], 2),
            round(input_data["compactness_mean"], 2),
            round(input_data["concavity_mean"], 2),
            round(input_data["concave points_mean"], 2),
            round(input_data["symmetry_mean"], 2),
            round(input_data["fractal_dimension_mean"], 2),
        ]
        standard = [
            round(input_data["radius_se"], 2),
            round(input_data["texture_se"], 2),
            round(input_data["perimeter_se"], 2),
            round(input_data["area_se"], 2),
            round(input_data["smoothness_se"], 2),
            round(input_data["compactness_se"], 2),
            round(input_data["concavity_se"], 2),
            round(input_data["concave points_se"], 2),
            round(input_data["symmetry_se"], 2),
            round(input_data["fractal_dimension_se"], 2),
        ]
        worst = [
            round(input_data["radius_worst"], 2),
            round(input_data["texture_worst"], 2),
            round(input_data["perimeter_worst"], 2),
            round(input_data["area_worst"], 2),
            round(input_data["smoothness_worst"], 2),
            round(input_data["compactness_worst"], 2),
            round(input_data["concavity_worst"], 2),
            round(input_data["concave points_worst"], 2),
            round(input_data["symmetry_worst"], 2),
            round(input_data["fractal_dimension_worst"], 2),
        ]

        chart_data = {
            "categories": CATEGORIES,
            "mean": mean,
            "standard": standard,
            "worst": worst,
        }

        return chart_data

    def display_explanations(self):
        return {
            "Mean Value": "Average or typical measurement for each category",
            "Standard Error": "Measure of variability or dispersion of the data",
            "Worst Value": "Worst-case scenario or maximum measurement observed for each category",
        }

    def save_prediction_result(
        self, user, response_instance, risk_level, risk_score, probabilities, chart_data
    ):
        # Check if there is an existing prediction result for the same questionnaire response
        existing_result = PredictionResult.objects.filter(
            user=user, questionnaire_response=response_instance
        ).first()

        if existing_result:
            # Update the existing result
            existing_result.risk_level = risk_level["level"]
            existing_result.risk_score = risk_score
            existing_result.dob = user.date_of_birth
            existing_result.probability_benign = probabilities[0][0]
            existing_result.probability_malignant = probabilities[0][1]
            existing_result.chart_data = chart_data
            existing_result.save()
        else:
            # Create a new prediction result
            PredictionResult.objects.create(
                user=user,
                questionnaire_response=response_instance,
                dob=user.date_of_birth,
                risk_level=risk_level["level"],
                risk_score=risk_score,
                probability_benign=probabilities[0][0],
                probability_malignant=probabilities[0][1],
                chart_data=chart_data,
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response_instance = self.object
        question_keys = response_instance.responses.all().values_list(
            "question_key",
            flat=True,
        )

        # Load default values
        default_values = self.get_default_values()

        user_responses = {}
        for _, k, v in QUESTIONS:
            user_responses[k] = v if k in question_keys else default_values.get(k, 0.00)

        probabilities = self.add_predictions(user_responses)

        chart_data = self.get_line_scatter_chart(user_responses)
        explanations = self.display_explanations()
        risk_level, risk_score = self.make_prediction(probabilities)
        risk_score = f"{risk_score * 100:.2f}"

        # Save the prediction result
        self.save_prediction_result(
            self.request.user,
            response_instance,
            risk_level,
            risk_score,
            probabilities,
            chart_data,
        )

        context.update(
            {
                "risk_level": risk_level,
                "risk_score": risk_score,
                "probability_benign": f"{probabilities[0][0]:.2f}",
                "probability_malignant": f"{probabilities[0][1]:.2f}",
                "risk_explanation": explanations,
                "chart_data": chart_data,
                "title_root": "Result",
            }
        )
        return context

results = PredictionView.as_view()

class PredictionResultView(FilterView):
    filterset_class = PredictionResultFilter
    model = PredictionResult
    template_name = "result-histores.html"
    context_object_name = "results"
    ordering = ["-submission_date", "-timestamp"]
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_root"] = "Prediction Results"
        return context

result_hostores = PredictionResultView.as_view()


from django.http import HttpResponse
import csv
import json
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls import reverse_lazy


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
        {
            "id": 1,
            "title": "Health Risk Assessment",
            "description": "Assessment to determine general health risks.",
            "creation_date": "2024-06-01",
            "status": "Active",
        },
        {
            "id": 2,
            "title": "Breast Cancer Awareness",
            "description": "Questionnaire to raise awareness about breast cancer.",
            "creation_date": "2024-05-15",
            "status": "Inactive",
        },
        # Add more questionnaire data here
    ]
    return render(
        request,
        "admin_questionnaire_management.html",
        {"questionnaires": questionnaires},
    )


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
# def result_hostores(request):
#     context = {"what_url": "MAIN DASHBOARD", "title_root": "Dashboard"}

#     return render(request, "result-histores.html", context)


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

    return render(request, "terms.html", context)


def profile(request):
    context = {
        "what_url": "MAIN DASHBOARD",
        "title_root": "Profile - Breast Cancer Prediction",
    }

    return render(request, "profile.html", context)

    # return render(request, "pwd-recovery.html", context)


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


def results1(request):
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

    return render(request, "contacts.html")


# class QuestionnaireView1(FormView):
#     template_name = "patients/questionnaier.html"
#     success_url = reverse_lazy("index")

#     def form_valid(self, form):
#         print("------------Process form data here----------------")
#         responses = form.cleaned_data
#         print(responses)
#         print("##############################################\n")
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         section_headers = ["Physical", "Skin", "Sensation", "Nipple", "Lumps"]
#         context["section_headers"] = section_headers
#         context["title_root"] = "Questionnaier"
#         return context


# class QuestionnaireView1(View):
#     template_name = "patients/questionnaier.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, self.get_context())

#     def post(self, request, *args, **kwargs):
#         form = request.POST
#         if form:
#             print("------------Process form data here----------------")
#             print(form)
#             print("##############################################\n")
#         return render(request, self.template_name, self.get_context())

#     def get_context(self):

#         context = {
#             "questions": QUESTIONS,
#             "section_headers": section_headers,
#             "title_root": "Questionnaier",
#         }
#         return context


# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.utils import timezone
# from django.contrib import messages
# from .models import QuestionnaireResponse, Response
# from .utils import QUESTIONS


# class QuestionnaireView(LoginRequiredMixin, View):
#     template_name = "patients/questionnaier.html"

#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, self.get_context())

#     def post(self, request, *args, **kwargs):
#         # Extract form data
#         form_data = request.POST

#         # Filter out questions with "Yes" responses (where answer is "on")
#         responses = {key: "Yes" for key, value in form_data.items() if value == "on"}

#         # Check if there are any "Yes" responses
#         if responses:
#             # Save responses to the database
#             self.save_responses(request.user, responses)
#             # Add a success message
#             messages.success(
#                 request, "Your responses have been successfully submitted."
#             )
#             # Redirect to a thank-you page or the same page
#             return redirect("summary")

#         # If no "Yes" responses, render the form again with an error message
#         messages.error(request, "Please respond to the questionnaire.")
#         return render(request, self.template_name, self.get_context())

#     def get_context(self):
#         # Group questions into sections
#         questions = QUESTIONS
#         context = {
#             "questions": questions,
#             "section_headers": section_headers,
#             "title_root": "Questionnaire",
#         }
#         return context

#     def save_responses(self, user, responses):
#         # Create a new QuestionnaireResponse instance
#         response_instance = QuestionnaireResponse(user=user)
#         response_instance.save()

#         # Save each response as a related object
#         for question, key in responses.items():
#             response_instance.responses.create(question_key=question)

#         # Optionally, perform any additional processing (e.g., send an email notification)


# questionnaier = QuestionnaireView.as_view()


# def summary_view1(request):
#     section_headers = [
#         "Physical Symptoms",
#         "Skin and Texture",
#         "Sensation",
#         "Nipple and Discharge",
#         "Lumps",
#     ]
#     # Assume this are the keys stored in our db
#     stored_db = [
#         "texture_mean",
#         "smoothness_mean",
#         "symmetry_mean",
#         "compactness_se",
#         "symmetry_se",
#         "fractal_dimension_se",
#         "radius_worst",
#         "smoothness_worst",
#     ]
#     questions = QUESTIONS
#     context = {
#         "section_headers": section_headers,
#         "title_root": "Summary",
#     }
#     return render(request, "summary.html", context)


# def summary_view2(request):

#     # Assume these are the keys stored in our db for the user's responses
#     stored_db = [
#         "texture_mean",
#         "smoothness_mean",
#         "symmetry_mean",
#         "compactness_se",
#         "symmetry_se",
#         "fractal_dimension_se",
#         "radius_worst",
#         "smoothness_worst",
#     ]

#     # Create a dictionary to hold questions grouped by section headers
#     grouped_questions = {header: [] for header in section_headers}
#     # Iterate over the stored_db keys and group questions accordingly
#     for key in stored_db:
#         for question, q_key, value in QUESTIONS:
#             if q_key == key:
#                 index = QUESTIONS.index((question, q_key, value))
#                 group_index = index // 6  # Determine the group based on position
#                 if group_index < len(section_headers):
#                     grouped_questions[section_headers[group_index]].append(
#                         (question, q_key, value)
#                     )

#     grouped_questions = {
#         header: questions
#         for header, questions in grouped_questions.items()
#         if questions
#     }

#     context = {
#         "grouped_questions": grouped_questions,
#         "title_root": "Summary",
#     }
#     return render(request, "summary.html", context)
