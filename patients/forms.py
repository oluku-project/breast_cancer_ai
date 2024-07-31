from django import forms
from patients.models import Contact, Feedback

class QuestionnaireForm(forms.Form):
    questions = [
        ("Do you experience a lump in the breast?", "radius_mean", 17.99),
        (
            "Do you have pain in the armpit or breast that does not change with the monthly cycle?",
            "texture_mean",
            21.25,
        ),
        (
            "Do you notice pitting or redness of the skin of the breast?",
            "perimeter_mean",
            132.90,
        ),
        (
            "Do you have any change in the size or shape of the breast?",
            "area_mean",
            1001.0,
        ),
        ("Do you experience discharge from the nipple?", "smoothness_mean", 0.1184),
        ("Do you have an inverted nipple?", "compactness_mean", 0.2776),
        ("Do you notice any rash on or around the nipple?", "concavity_mean", 0.3001),
        (
            "Do you experience swelling in the armpit or around the collarbone?",
            "concave_points_mean",
            0.1471,
        ),
        (
            "Do you have changes in the skin texture (e.g., puckering or dimpling)?",
            "symmetry_mean",
            0.1812,
        ),
        (
            "Do you notice any areas of thickened tissue in the breast?",
            "fractal_dimension_mean",
            0.0628,
        ),
        ("Do you have skin irritation or dimpling?", "radius_se", 0.2500),
        (
            "Do you notice any redness or enlarged pores on the breast skin?",
            "texture_se",
            1.22,
        ),
        ("Do you feel any hardness or firmness in the breast?", "perimeter_se", 2.80),
        ("Do you experience unusual warmth in the breast?", "area_se", 40.0),
        (
            "Do you have persistent itching of the breast or nipple?",
            "smoothness_se",
            0.01,
        ),
        (
            "Do you observe changes in the breast skin (e.g., ulceration)?",
            "compactness_se",
            0.03,
        ),
        ("Do you have prominent veins on the breast?", "concavity_se", 0.03),
        (
            "Do you notice any changes in the nipple shape or appearance?",
            "concave_points_se",
            0.01,
        ),
        (
            "Do you experience peeling or flaking of the nipple skin?",
            "symmetry_se",
            0.02,
        ),
        (
            "Do you have any changes in the appearance of the nipple?",
            "fractal_dimension_se",
            0.003,
        ),
        ("Do you experience a sudden change in breast size?", "radius_worst", 25.41),
        (
            "Do you have noticeable asymmetry between the breasts?",
            "texture_worst",
            39.28,
        ),
        ("Do you observe swelling of the entire breast?", "perimeter_worst", 188.50),
        (
            "Do you experience skin changes such as puckering or dimpling?",
            "area_worst",
            2501.0,
        ),
        (
            "Do you notice thickened areas or lumps in the breast?",
            "smoothness_worst",
            0.1447,
        ),
        (
            "Do you have unexplained pain or tenderness in the breast?",
            "compactness_worst",
            0.3454,
        ),
        (
            "Do you feel any lumps or masses in the breast tissue?",
            "concavity_worst",
            0.4268,
        ),
        (
            "Do you observe any discharge from the nipples (other than breast milk)?",
            "concave_points_worst",
            0.2012,
        ),
        (
            "Do you have unusual warmth or redness in the breast?",
            "symmetry_worst",
            0.2901,
        ),
        (
            "Do you notice any visible veins or blood vessels on the breast?",
            "fractal_dimension_worst",
            0.0834,
        ),
    ]

    for question, key, _ in questions:
        locals()[key] = forms.ChoiceField(
            label=question,
            choices=[("No", "No"), ("Yes", "Yes")],
            widget=forms.RadioSelect,
            required=True,
        )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["message", "rating"]


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email","subject", "message"]
