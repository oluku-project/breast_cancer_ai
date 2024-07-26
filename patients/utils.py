QUESTIONS = [
    ("Do you feel a lump in your breast?", "radius_mean", 17.99),
    (
        "Do you have consistent pain in your armpit or breast?",
        "texture_mean",
        21.25,
    ),
    (
        "Do you notice any redness or pitting on your breast skin?",
        "perimeter_mean",
        132.90,
    ),
    ("Has the size or shape of your breast changed recently?", "area_mean", 1001.0),
    (
        "Do you experience nipple discharge (not breast milk)?",
        "smoothness_mean",
        0.1184,
    ),
    ("Is your nipple inverted?", "compactness_mean", 0.2776),
    ("Do you have a rash on or around your nipple?", "concavity_mean", 0.3001),
    (
        "Is there swelling in your armpit or around your collarbone?",
        "concave points_mean",
        0.1471,
    ),
    (
        "Have you noticed any puckering or dimpling of the breast skin?",
        "symmetry_mean",
        0.1812,
    ),
    (
        "Do you feel areas of thickened tissue in your breast?",
        "fractal_dimension_mean",
        0.0628,
    ),
    (
        "Do you have persistent breast skin irritation or dimpling?",
        "radius_se",
        0.2500,
    ),
    (
        "Have you noticed redness or enlarged pores on your breast?",
        "texture_se",
        1.22,
    ),
    ("Do you feel any hardness or firmness in your breast?", "perimeter_se", 2.80),
    ("Do you experience unusual warmth in your breast?", "area_se", 40.0),
    (
        "Do you have persistent itching of your breast or nipple?",
        "smoothness_se",
        0.01,
    ),
    (
        "Have you observed any ulceration on your breast skin?",
        "compactness_se",
        0.03,
    ),
    ("Do you see prominent veins on your breast?", "concavity_se", 0.03),
    ("Has your nipple changed shape or appearance?", "concave points_se", 0.01),
    (
        "Do you experience peeling or flaking of your nipple skin?",
        "symmetry_se",
        0.02,
    ),
    (
        "Have you noticed any changes in the appearance of your nipple?",
        "fractal_dimension_se",
        0.003,
    ),
    (
        "Have you experienced a sudden change in your breast size?",
        "radius_worst",
        25.41,
    ),
    ("Do you notice asymmetry between your breasts?", "texture_worst", 39.28),
    ("Is there swelling of your entire breast?", "perimeter_worst", 188.50),
    (
        "Do you see skin changes such as puckering or dimpling?",
        "area_worst",
        2501.0,
    ),
    (
        "Do you feel thickened areas or lumps in your breast?",
        "smoothness_worst",
        0.1447,
    ),
    (
        "Do you have unexplained pain or tenderness in your breast?",
        "compactness_worst",
        0.3454,
    ),
    (
        "Do you feel lumps or masses in your breast tissue?",
        "concavity_worst",
        0.4268,
    ),
    (
        "Do you experience nipple discharge that isn't breast milk?",
        "concave points_worst",
        0.2012,
    ),
    (
        "Do you have unusual warmth or redness in your breast?",
        "symmetry_worst",
        0.2901,
    ),
    (
        "Do you notice any visible veins or blood vessels on your breast?",
        "fractal_dimension_worst",
        0.0834,
    ),
]
CATEGORIES = [
    "Lump in Breast",
    "Pain in Armpit/Breast",
    "Redness of Breast Skin",
    "Change in Size/Shape",
    "Nipple Discharge",
    "Inverted Nipple",
    "Rash on Nipple",
    "Swelling in Armpit/Collarbone",
    "Skin Texture Changes",
    "Thickened Tissue Areas",
]
section_headers = [
    "Physical Symptoms",
    "Skin and Texture",
    "Sensation",
    "Nipple and Discharge",
    "Lumps",
]
RISK_LEVEL = [
    {
        "level": "Low",
        "info": "Your risk level based on the assessment is <strong>Low</strong>. This indicates a lower likelihood of breast cancer. Regular screenings and a healthy lifestyle are recommended to maintain this low risk. Please continue to monitor for any unusual changes and consult your healthcare provider if you have concerns.",
        "description": [
            "With a score of {score}%, your risk of breast cancer is considered low. It is essential to continue regular check-ups and adopt healthy lifestyle habits to keep this risk minimal.",
            "A score of {score}% places you in the low-risk category. Maintaining a balanced diet, regular exercise, and routine medical screenings can help manage this risk effectively.",
        ],
        "next_steps": [
            {
                "title": "Continue Regular Check-Ups",
                "subtitle": "Maintain Routine Screenings",
                "messages": [
                    "Continue regular self-examinations and annual mammograms as recommended by your healthcare provider.",
                    "Maintain a healthy lifestyle, including a balanced diet and regular physical activity.",
                    "Stay informed about breast health and promptly report any changes to your healthcare provider.",
                ],
            },
            {
                "title": "Maintain Healthy Lifestyle",
                "subtitle": "Healthy Habits",
                "messages": [
                    "Maintain a healthy diet rich in fruits, vegetables, and whole grains.",
                    "Engage in regular physical activity, aiming for at least 150 minutes of moderate exercise per week.",
                    "Avoid smoking and limit alcohol consumption to reduce overall cancer risk.",
                ],
            },
        ],
        "resources": [
            {
                "text": "Breast Cancer Screening Guidelines",
                "url": "https://www.cancer.org/cancer/screening/get-screened.html",
            },
            {
                "text": "Healthy Lifestyle Tips",
                "url": "https://www.cancer.org/cancer/risk-prevention/diet-physical-activity/diet-and-physical-activity.html",
            },
        ],
        "recommendations": [
            {
                "title": "Schedule Routine Mammograms",
                "message": "Schedule routine mammograms as recommended by your healthcare provider, typically every 1-2 years for women over 40.",
            },
            {
                "title": "Stay Informed About Breast Health",
                "message": "Stay informed about breast health and perform regular self-examinations to detect any changes early.",
            },
            {
                "title": "Discuss Family History",
                "message": "Discuss any family history of breast cancer with your healthcare provider to ensure appropriate monitoring.",
            },
        ],
    },
    {
        "level": "Moderate",
        "info": "Your risk level based on the assessment is <strong>Moderate</strong>. This suggests an intermediate likelihood of breast cancer. It is important to consult with your healthcare provider to discuss your risk factors in detail. They may recommend more frequent screenings or preventive measures to manage your risk effectively.",
        "description": [
            "With a score of {score}%, your breast cancer risk is moderate. A detailed discussion with your healthcare provider about personalized screening plans and lifestyle adjustments is recommended.",
            "A score of {score}% indicates a moderate risk. Engaging in regular screenings and potentially adopting preventive measures as advised by your healthcare provider can help manage this risk.",
        ],
        "next_steps": [
            {
                "title": "Schedule a Consultation",
                "subtitle": "Discuss Risk Factors",
                "messages": [
                    "Schedule a detailed consultation with your healthcare provider to discuss your risk factors and create a personalized screening plan.",
                    "Consider lifestyle changes that can reduce your risk, such as a healthy diet and regular exercise.",
                    "Stay vigilant about breast health and promptly report any changes to your healthcare provider.",
                ],
            },
            {
                "title": "Lifestyle Adjustments",
                "subtitle": "Reduce Your Risk",
                "messages": [
                    "Increase the frequency of mammograms to annually, or as advised by your healthcare provider.",
                    "Consider lifestyle changes, such as adopting a diet high in antioxidants and omega-3 fatty acids.",
                    "Discuss the possibility of genetic testing if there is a family history of breast cancer.",
                ],
            },
        ],
        "resources": [
            {
                "text": "Understanding Your Risk",
                "url": "https://www.breastcancer.org/risk/understand",
            },
            {
                "text": "Preventive Health Measures",
                "url": "https://www.cdc.gov/chronic-disease/prevention/index.html",
            },
        ],
        "recommendations": [
            {
                "title": "Maintain a Healthy Weight",
                "message": "Maintain a healthy weight through balanced nutrition and regular exercise.",
            },
            {
                "title": "Consider Risk-Reducing Medications",
                "message": "Consider medications such as tamoxifen or raloxifene for risk reduction if recommended by your doctor.",
            },
            {
                "title": "Stay Vigilant for Changes",
                "message": "Stay vigilant for any changes in your breast tissue and report them to your healthcare provider immediately.",
            },
        ],
    },
    {
        "level": "High",
        "info": "Your risk level based on the assessment is <strong>High</strong>. This indicates a higher likelihood of breast cancer. Immediate consultation with your healthcare provider is crucial for a comprehensive evaluation. They will guide you on the next steps, which may include diagnostic tests and potential treatment options to address your risk.",
        "description": [
            "With a score of {score}%, your risk is high. It is crucial to seek immediate medical advice for a comprehensive evaluation and to discuss potential diagnostic tests and treatment options.",
            "A score of {score}% signifies a high risk of breast cancer. Prompt consultation with your healthcare provider is necessary to determine the appropriate next steps, including possible diagnostic procedures and interventions.",
        ],
        "next_steps": [
            {
                "title": "Urgent Consultation",
                "subtitle": "Seek Immediate Advice",
                "messages": [
                    "Arrange an urgent appointment with your healthcare provider for a comprehensive evaluation.",
                    "Be prepared to discuss potential diagnostic tests and treatment options with your healthcare provider.",
                    "Follow your healthcare provider's recommendations closely and stay informed about the latest advancements in breast cancer prevention and treatment.",
                ],
            },
            {
                "title": "Advanced Diagnostic Tests",
                "subtitle": "Detailed Evaluation",
                "messages": [
                    "Schedule an immediate appointment with a breast cancer specialist for a detailed evaluation.",
                    "Undergo advanced diagnostic tests such as MRI or ultrasound in addition to routine mammograms.",
                    "Discuss the potential benefits of risk-reducing medications or prophylactic surgery (e.g., mastectomy) with your healthcare provider.",
                ],
            },
        ],
        "resources": [
            {
                "text": "Steps to Take After a High-Risk Assessment",
                "url": "https://www.uchealth.com/en/media-room/articles/breast-cancer-risk-assessment",
            },
            {
                "text": "Breast Cancer Treatment Options",
                "url": "https://www.breastcancer.org/treatment",
            },
        ],
        "recommendations": [
            {
                "title": "Genetic Counseling and Testing",
                "message": "Consider genetic counseling and testing, especially if there is a significant family history of breast cancer.",
            },
            {
                "title": "Personalized Monitoring Plan",
                "message": "Develop a personalized monitoring plan with frequent clinical breast exams and imaging tests.",
            },
            {
                "title": "Stay Informed About Advances",
                "message": "Stay informed about the latest research and advances in breast cancer prevention and treatment.",
            },
            {
                "title": "Engage in Support Groups",
                "message": "Engage in support groups or counseling to address any emotional or psychological impacts of a high-risk diagnosis.",
            },
        ],
    },
]

class HelpResponse:

    def fetchRespondedQuestions(self, response_instance):
        grouped_questions = {header: [] for header in section_headers}
        for response in response_instance.responses.all():
            question = next(q for q in QUESTIONS if q[1] == response.question_key)
            index = QUESTIONS.index(question) // 6
            section_header = section_headers[index]
            grouped_questions[section_header].append(question[0])

        # Remove empty groups
        grouped_questions = {k: v for k, v in grouped_questions.items() if v}
        return grouped_questions
