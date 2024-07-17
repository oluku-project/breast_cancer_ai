from django.core.management.base import BaseCommand
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle5 as pickle
from sklearn.ensemble import RandomForestClassifier
from BreastCancerAI import settings
from pathlib import Path


def get_clean_data():
    data = pd.read_csv(f"{settings.STATICFILES_DIRS[0]}/model/data.csv")

    data = data.drop(["Unnamed: 32", "id"], axis=1)

    data["diagnosis"] = data["diagnosis"].map({"M": 1, "B": 0})
    return data


def create_model(data):
    X = data.drop("diagnosis", axis=1)
    y = data["diagnosis"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Fit the scaler
    scaler = StandardScaler()
    x_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train the model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # # Alternatively, use RandomForestClassifier
    # model = RandomForestClassifier(n_estimators=100, random_state=42)
    # model.fit(X_train_scaled, y_train)

    # Test the model
    y_pred = model.predict(X_test)
    print("Accuracy of our model: ", accuracy_score(y_test, y_pred))
    print("Classification report: \n", classification_report(y_test, y_pred))

    return model, scaler


class Command(BaseCommand):
    help = "Train a machine learning model and save it."

    def handle(self, *args, **kwargs):
        data = get_clean_data()

        model, scaler = create_model(data)

        model_path = f"{settings.STATICFILES_DIRS[0]}/model/model.pkl"
        scaler_path = f"{settings.STATICFILES_DIRS[0]}/model/scaler.pkl"

        with open(model_path, "wb") as model_file:
            pickle.dump(model, model_file)

        with open(scaler_path, "wb") as scaler_file:
            pickle.dump(scaler, scaler_file)

        self.stdout.write(
            self.style.SUCCESS("Successfully trained and saved the model.")
        )
