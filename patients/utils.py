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
FAQS = [
    {
        "heading": "General Information",
        "questions": [
            {
                "question": "What is the Breast Cancer Prediction Project?",
                "answer": "The Breast Cancer Prediction Project is an initiative designed to develop and implement machine learning models to predict the likelihood of breast cancer in individuals based on various risk factors.",
            },
            {
                "question": "What types of data are used in the prediction models?",
                "answer": "The models use data such as demographic information, medical history, genetic factors, lifestyle habits, and results from medical tests (e.g., mammograms, biopsies).",
            },
            {
                "question": "How does machine learning improve breast cancer prediction?",
                "answer": "Machine learning algorithms can analyze large datasets to identify patterns and correlations that might not be apparent through traditional analysis, leading to more accurate and personalized risk assessments.",
            },
            {
                "question": "Who can benefit from this project?",
                "answer": "This project is beneficial for women at risk of breast cancer, healthcare providers seeking to improve early detection, and researchers looking to enhance predictive models for breast cancer.",
            },
            {
                "question": "How accurate are the machine learning models used in the project?",
                "answer": "The accuracy of the models depends on the quality and quantity of the data used for training. While machine learning models can provide high accuracy, they are not infallible and should be used in conjunction with professional medical advice.",
            },
            {
                "question": "What are the primary goals of this project?",
                "answer": "The main goals are to improve early detection of breast cancer, provide personalized risk assessments, and support healthcare providers in making informed decisions about patient care.",
            },
            {
                "question": "How is patient privacy maintained in this project?",
                "answer": "Patient data is anonymized and stored securely. Only authorized personnel have access to the data, and strict protocols are in place to ensure confidentiality and compliance with data protection regulations.",
            },
            {
                "question": "Can the prediction models be integrated into existing healthcare systems?",
                "answer": "Yes, the models are designed to be compatible with existing electronic health record (EHR) systems and can be integrated to enhance clinical decision support tools.",
            },
            {
                "question": "What challenges does the project face?",
                "answer": "Challenges include ensuring the diversity and quality of the data, maintaining patient privacy, addressing ethical considerations, and continuously updating models to reflect new research findings.",
            },
            {
                "question": "How can healthcare providers use the predictions?",
                "answer": "Healthcare providers can use the predictions to identify high-risk individuals, recommend appropriate screenings, and discuss preventive measures or treatment options with their patients.",
            },
            {
                "question": "What is the significance of using AI in breast cancer prediction?",
                "answer": "AI can process vast amounts of data quickly and accurately, leading to earlier detection and potentially better outcomes for patients by enabling timely intervention.",
            },
            {
                "question": "How does the project address false positives and false negatives?",
                "answer": "The models are continuously refined to minimize false positives and negatives. Cross-validation, rigorous testing, and feedback loops with clinical data help improve model accuracy and reliability.",
            },
            {
                "question": "What are the future directions of this project?",
                "answer": "Future directions include expanding the dataset, incorporating new risk factors, improving model algorithms, and exploring collaborations with healthcare institutions for real-world implementation.",
            },
            {
                "question": "How can individuals participate in this project?",
                "answer": "Individuals can participate by contributing their data through clinical trials or registries, and by engaging with healthcare providers who use the prediction tools developed by the project.",
            },
            {
                "question": "What impact does this project aim to have on public health?",
                "answer": "The project aims to reduce the incidence of late-stage breast cancer diagnoses, improve survival rates, and contribute to the overall knowledge and management of breast cancer through advanced predictive analytics.",
            },
        ],
    },
    {
        "heading": "Results Interpretation",
        "questions": [
            {
                "question": "How should I interpret the risk score provided by the model?",
                "answer": "The risk score indicates the likelihood of developing breast cancer based on the input data. Higher scores suggest a higher risk, but it is important to discuss the results with a healthcare provider for a comprehensive interpretation.",
            },
            {
                "question": "What do the terms 'benign' and 'malignant' mean in the results?",
                "answer": "'Benign' indicates non-cancerous conditions, while 'malignant' indicates cancerous growths. The model provides probabilities for both to help assess the risk.",
            },
            {
                "question": "How can I understand the probabilities provided in the prediction?",
                "answer": "The probabilities for benign and malignant conditions are expressed as percentages. These indicate the likelihood of each condition based on the input data.",
            },
            {
                "question": "What should I do if my prediction indicates a high risk of breast cancer?",
                "answer": "If the prediction indicates a high risk, it is important to consult with a healthcare provider to discuss further diagnostic tests, preventive measures, and possible treatment options.",
            },
            {
                "question": "Can the prediction results change over time?",
                "answer": "Yes, prediction results can change as new data becomes available or if there are changes in risk factors such as age, lifestyle, or medical history.",
            },
            {
                "question": "Are the prediction results definitive?",
                "answer": "No, the results are not definitive. They are probabilistic estimates based on the input data and should be used as part of a broader diagnostic process involving healthcare professionals.",
            },
            {
                "question": "How often should I use the prediction tool?",
                "answer": "The frequency of use depends on individual risk factors and recommendations from healthcare providers. Regular updates to the data can help maintain accurate predictions.",
            },
        ],
    },
    {
        "heading": "Data Privacy and Security",
        "questions": [
            {
                "question": "How is my personal data protected in this project?",
                "answer": "Personal data is anonymized and encrypted to protect privacy. Strict access controls and data protection protocols are in place to ensure confidentiality.",
            },
            {
                "question": "Who has access to my data?",
                "answer": "Only authorized personnel involved in the project have access to the data. Access is granted based on the need to know and in compliance with data protection regulations.",
            },
            {
                "question": "Can I withdraw my data from the project?",
                "answer": "Yes, participants can request to withdraw their data from the project at any time. Procedures are in place to handle such requests while maintaining data integrity.",
            },
            {
                "question": "What measures are taken to ensure data security?",
                "answer": "Data security measures include encryption, secure storage, access controls, and regular security audits to protect against unauthorized access and data breaches.",
            },
            {
                "question": "Will my data be shared with third parties?",
                "answer": "Data may be shared with research collaborators or healthcare providers only with explicit consent from participants and under strict confidentiality agreements.",
            },
        ],
    },
    {
        "heading": "Technical Aspects",
        "questions": [
            {
                "question": "What machine learning algorithms are used in the project?",
                "answer": "The project employs various algorithms such as logistic regression, decision trees, random forests, support vector machines, and neural networks.",
            },
            {
                "question": "How is the model trained and validated?",
                "answer": "The model is trained using historical data and validated through cross-validation techniques to ensure accuracy and generalizability.",
            },
            {
                "question": "What programming languages and tools are used in the project?",
                "answer": "Common programming languages and tools used include Python, R, TensorFlow, Scikit-learn, and Pandas.",
            },
            {
                "question": "How are the models updated and maintained?",
                "answer": "Models are regularly updated with new data and retrained to improve performance. Continuous monitoring and evaluation ensure they remain accurate and relevant.",
            },
            {
                "question": "Can the model be customized for different populations?",
                "answer": "Yes, the model can be adapted to account for demographic and genetic variations across different populations to improve accuracy and relevance.",
            },
        ],
    },
    {
        "heading": " Clinical Applications",
        "questions": [
            {
                "question": "How can healthcare providers integrate the prediction tool into their practice?",
                "answer": "Healthcare providers can integrate the tool into their electronic health records (EHR) systems and use it as part of routine screenings and risk assessments.",
            },
            {
                "question": "What benefits does the prediction tool offer to clinicians?",
                "answer": "The tool provides clinicians with additional insights into patient risk profiles, helping them make more informed decisions about screening and preventive measures.",
            },
            {
                "question": "How can the prediction tool support early detection of breast cancer?",
                "answer": "By identifying high-risk individuals early, the tool can prompt timely screenings and interventions, potentially leading to earlier detection and better outcomes.",
            },
            {
                "question": "What training is required for healthcare providers to use the tool?",
                "answer": "Minimal training is required, focusing on understanding the results and integrating the tool into clinical workflows. Detailed user guides and support are provided.",
            },
            {
                "question": "Can the tool be used in conjunction with other diagnostic methods?",
                "answer": "Yes, the tool is designed to complement other diagnostic methods such as mammograms and biopsies, providing a more comprehensive assessment of breast cancer risk.",
            },
        ],
    },
    {
        "heading": "Research Development",
        "questions": [
            {
                "question": "What are the key research objectives of the project?",
                "answer": "Key objectives include improving model accuracy, expanding the dataset, and exploring new risk factors and biomarkers for breast cancer prediction.",
            },
            {
                "question": "How can researchers contribute to the project?",
                "answer": "Researchers can contribute by providing data, collaborating on model development, and conducting studies to validate and refine the prediction models.",
            },
            {
                "question": "What advancements have been made since the project's inception?",
                "answer": "Significant advancements include the development of more accurate models, integration with healthcare systems, and publication of research findings.",
            },
            {
                "question": "How is the project funded?",
                "answer": "The project is funded through a combination of grants, institutional support, and contributions from research collaborators and healthcare organizations.",
            },
            {
                "question": "What are the long-term goals of the project?",
                "answer": "Long-term goals include widespread adoption of the prediction tool in clinical practice, continuous improvement of model performance, and significant contributions to breast cancer research and prevention.",
            },
        ],
    },
]
RATE_CHOICES = [
    (1, "Very Poor"),
    (2, "Poor"),
    (3, "Average"),
    (4, "Good"),
    (5, "Excellent"),
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
