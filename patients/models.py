from django.db import models
from django.db.models.functions import Now


class STATE(models.TextChoices):
    INITIATE = "Initiate", "Initiate"
    START = "Start", "Start"
    COMPLETE = "Complete", "Complete"


class QuestionnaireResponse(models.Model):
    user = models.ForeignKey("accounts.account", on_delete=models.CASCADE)
    progress = models.FloatField(db_default=0)
    submission_date = models.DateTimeField(db_default=Now())
    updated_date = models.DateTimeField(db_default=Now(), auto_now=True)
    state = models.CharField(max_length=10, choices=STATE, default=STATE.INITIATE)

    def __str__(self):
        return f"{self.user.username} - {self.submission_date.strftime('%Y-%m-%d %H:%M:%S')}"


class Response(models.Model):
    questionnaire_response = models.ForeignKey(
        QuestionnaireResponse, related_name="responses", on_delete=models.CASCADE
    )
    question_key = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.question_key}: {self.questionnaire_response}"


class PredictionResultManager(models.Manager):
    def get_queryset(self):
        if not hasattr(self, "_user") or not (
            self._user.is_superuser or self._user.is_staff
        ):
            return super().get_queryset().filter(deleted=False)
        return super().get_queryset()

    def for_user(self, user):
        manager = self.__class__()
        manager._user = user
        manager.model = self.model
        manager._db = self._db
        return manager


class PredictionResult(models.Model):
    user = models.ForeignKey("accounts.account", on_delete=models.CASCADE)
    questionnaire_response = models.ForeignKey(
        QuestionnaireResponse, on_delete=models.CASCADE
    )
    dob = models.DateField(verbose_name="Birthday", null=True)
    risk_level = models.CharField(max_length=20)
    risk_score = models.DecimalField(max_digits=5, decimal_places=2)
    probability_benign = models.DecimalField(max_digits=5, decimal_places=2)
    probability_malignant = models.DecimalField(max_digits=5, decimal_places=2)
    chart_data = models.JSONField()
    submission_date = models.DateTimeField(db_default=Now())
    timestamp = models.DateTimeField(db_default=Now(), auto_now=True)

    deleted = models.BooleanField(default=False)

    objects = PredictionResultManager()

    def benign(self):
        return f"{self.probability_benign * 100:.2f}"

    def malignant(self):
        return f"{self.probability_malignant * 100:.2f}"

    def __str__(self):
        return f"Prediction for {self.user.username} at {self.timestamp}"

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(db_default=Now())

    def __str__(self):
        return f"Feedback from {self.name} at {self.submitted_at}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(db_default=Now())

    def __str__(self):
        return (
            f"Contact request from {self.name} - {self.subject} at {self.submitted_at}"
        )
