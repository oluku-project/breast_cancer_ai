from django.db import models
from django.db.models.functions import Now


class QuestionnaireResponse(models.Model):
    user = models.ForeignKey("accounts.account", on_delete=models.CASCADE)
    progress = models.FloatField(db_default=0)
    submission_date = models.DateTimeField(db_default=Now())
    updated_date = models.DateTimeField(db_default=Now(), auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.submission_date.strftime('%Y-%m-%d %H:%M:%S')}"


class Response(models.Model):
    questionnaire_response = models.ForeignKey(
        QuestionnaireResponse, related_name="responses", on_delete=models.CASCADE
    )
    question_key = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.question_key}: {self.questionnaire_response}"

from django.db import models


class PredictionResult(models.Model):
    user = models.ForeignKey("accounts.account", on_delete=models.CASCADE)
    questionnaire_response = models.ForeignKey(
        QuestionnaireResponse, on_delete=models.CASCADE
    )
    risk_level = models.CharField(max_length=20)
    risk_score = models.DecimalField(max_digits=5, decimal_places=2)
    probability_benign = models.DecimalField(max_digits=5, decimal_places=2)
    probability_malignant = models.DecimalField(max_digits=5, decimal_places=2)
    chart_data = models.JSONField()
    submission_date = models.DateTimeField(db_default=Now())
    timestamp = models.DateTimeField(db_default=Now(), auto_now=True)

    def __str__(self):
        return f"Prediction for {self.user.username} at {self.timestamp}"
