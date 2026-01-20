#  Organ Transplant Decision Support System

An AI-assisted, explainable clinical decision support system designed to help transplant physicians evaluate patient eligibility, urgency, and risk for solid organ transplantation.

> ⚠️ **Disclaimer:**  
> This system is intended to support clinical decision-making.  
> It does **not** replace physician judgment or institutional transplant protocols.

---

## 📌 Project Overview

Organ transplantation is a high-risk, time-sensitive medical decision involving multiple clinical, immunological, and ethical factors.  
This project presents a **doctor-centric dashboard** that:

- Accepts structured patient clinical data
- Performs rule-based clinical safety checks
- Uses machine learning to estimate **1-year post-transplant survival**
- Provides **explainable outputs** suitable for clinical interpretation

The system is designed as a **decision-support tool**, not an autonomous decision-maker.

---

## 🧠 System Capabilities

### ✅ Clinical Logic (Rule-Based)
- Organ-specific severity interpretation (GFR, MELD, EF)
- Contraindication detection (infection, cancer, comorbidities)
- Risk stratification
- Urgency assessment
- Eligibility determination

### 🤖 AI / Machine Learning
- Predicts **1-year survival probability**
- Trained on synthetic transplant outcome data
- Uses classical ML (Random Forest / Logistic Regression)
- Outputs are probabilistic and non-deterministic

### 🔍 Explainability
- Highlights key contributing factors (e.g., infection, age, PRA)
- Provides transparent, clinician-readable explanations
- Avoids black-box decision-making

---

## 🖥️ Dashboard Features

- Clean, hospital-grade UI built with **Streamlit**
- Patient identification and clinical context
- Immunological compatibility profile
- AI-assisted risk metrics
- Explainability section
- Final clinical summary
- Clinician remarks section
- Audit & ethics information

---

## 🏗️ System Architecture

The following diagram illustrates the high-level architecture of the system:

📷 **Architecture Diagram:**  
<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/fb88dac4-a40f-4a7d-84df-449a02552024" />

*System Architecture*


**Architecture Flow:**

1. Patient clinical data input
2. Clinical rule-based evaluation
3. Feature engineering
4. Machine learning inference
5. Explainability generation
6. Physician-facing dashboard

---

## 📂 Project Structure

Organ_Transplant_AI/
├── app/
│ └── dashboard.py
├── clinical_logic/
│ ├── organ_severity.py
│ ├── contraindications.py
│ ├── risk_engine.py
│ ├── urgency.py
│ └── eligibility.py
├── ml/
│ ├── feature_builder.py
│ ├── inference.py
│ ├── train_survival_model.py
│ └── survival_model.pkl
├── utils/
│ └── explainability.py
├── data/
│ └── transplant_survival.csv
├── requirements.txt
└── README.md


---

## 🧪 Dataset

- **transplant_survival.csv**
- Synthetic dataset (200–500 rows)
- Columns include:
  - Age
  - Organ type
  - Severity score
  - ICU admission
  - Infection
  - PRA
  - HLA mismatch
  - Cancer status
  - 1-year survival outcome

⚠️ No real patient data is used.

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt

2️⃣ Train the model (once)
python ml/train_survival_model.py

3️⃣ Run the dashboard
streamlit run app/dashboard.py

🧑‍⚕️ Intended Users

Transplant physicians

Clinical researchers

Medical AI students

Academic evaluation (projects, thesis, viva)

🛡️ Ethics & Safety

No automated clinical decisions

Explainable outputs only

Clear disclaimers

Designed to align with clinical governance principles

📚 Technologies Used

Python

Streamlit

Pandas, NumPy

Scikit-learn

Joblib

📈 Future Enhancements

Real-world dataset integration

Organ-specific ML models

SHAP-based explainability

Multi-center validation

Secure authentication

EHR integration (FHIR)

👩‍⚕️👨‍⚕️ Final Note

This project demonstrates how AI can assist—but not replace—clinical expertise, especially in high-stakes medical decisions like organ transplantation.
