from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Now


class QuestionnaireResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateTimeField(db_default=Now())
    updated_date = models.DateTimeField(db_default=Now(), auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.submission_date.strftime('%Y-%m-%d %H:%M:%S')}"


class Response(models.Model):
    questionnaire_response = models.ForeignKey(
        QuestionnaireResponse, related_name="responses", on_delete=models.CASCADE
    )
    question_key = models.CharField(max_length=50)
    answer = models.CharField(
        max_length=3, choices=[("Yes", "Yes"), ("No", "No")], default="No"
    )

    def __str__(self):
        return f"{self.question_key}: {self.answer}"
