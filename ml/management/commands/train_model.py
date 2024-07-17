import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Train the machine learning model"

    def handle(self, *args, **kwargs):
        data_path = os.path.join(settings.STATIC_ROOT, "ml/data.csv")
        data = self.get_clean_data(data_path)
        model, scaler = self.create_model(data)
        self.save_model_and_scaler(model, scaler)
        self.stdout.write(
            self.style.SUCCESS("Successfully trained the model and saved it.")
        )

    def get_clean_data(self, data_path):
        data = pd.read_csv(data_path)
        data = data.drop(["Unnamed: 32", "id"], axis=1)
        data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
        return data

    def create_model(self, data):
        X = data.drop("diagnosis", axis=1)
        y = data["diagnosis"]

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Fit the scaler
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # Train the model
        model = LogisticRegression()
        model.fit(X_train, y_train)

        # Test model
        y_pred = model.predict(X_test)
        print("Accuracy of our model: ", accuracy_score(y_test, y_pred))
        print("Classification report: \n", classification_report(y_test, y_pred))

        return model, scaler

    def save_model_and_scaler(self, model, scaler):
        model_path = os.path.join(settings.BASE_DIR, "ml/model.pkl")
        scaler_path = os.path.join(settings.BASE_DIR, "ml/scaler.pkl")

        with open(model_path, "wb") as model_file:
            pickle.dump(model, model_file)

        with open(scaler_path, "wb") as scaler_file:
            pickle.dump(scaler, scaler_file)
