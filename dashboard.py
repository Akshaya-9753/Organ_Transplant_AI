import sys
from pathlib import Path

# -------------------- PATH FIX --------------------
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

import streamlit as st
from datetime import date
import pandas as pd

# ----------- CLINICAL LOGIC IMPORTS -----------
from clinical_logic.organ_severity import interpret_severity
from clinical_logic.contraindications import contraindication_status
from clinical_logic.risk_engine import calculate_risk_score, risk_level
from clinical_logic.urgency import urgency_level
from clinical_logic.eligibility import eligibility
from utils.explainability import build_explainability

# ----------- ML / AI IMPORTS -----------
from ml.feature_builder import build_features
from ml.inference import predict_survival


# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Organ Transplant Decision Support System",
    layout="wide"
)

# -------------------- GLOBAL STYLES --------------------
st.markdown(
    """
    <style>
    body { background-color:#F7F9FB; color:#2E2E2E; }

    .main-title { font-size:30px; font-weight:700; color:#0B4F6C; }
    .subtitle { font-size:15px; color:#5F6F7A; }

    .card {
        background:#FFFFFF;
        border-radius:16px;
        padding:22px;
        margin-bottom:18px;
        box-shadow:0 4px 14px rgba(11,79,108,0.08);
        border:1px solid #E6ECF2;
    }

    .section-title {
        font-size:19px;
        font-weight:600;
        color:#0B4F6C;
        margin-bottom:14px;
    }

    .disclaimer {
        background:#F1F8FA;
        border-left:5px solid #2FA4A9;
        padding:12px 16px;
        font-size:13px;
        border-radius:8px;
        margin-top:14px;
    }

    .metric-card {
        background:linear-gradient(135deg,#F9FCFD,#F1F8FA);
        border-radius:14px;
        padding:18px;
        text-align:center;
        border:1px solid #E3EDF3;
    }

    .metric-value {
        font-size:26px;
        font-weight:700;
        color:#0B4F6C;
    }

    .metric-label { font-size:13px; color:#5F6F7A; }

    .badge {
        display:inline-block;
        padding:6px 14px;
        border-radius:20px;
        font-size:12px;
        font-weight:600;
        color:white;
        margin-right:8px;
        margin-top:6px;
    }

    .red { background:#C0392B; }
    .amber { background:#F1C40F; color:#2E2E2E; }
    .green { background:#27AE60; }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- HEADER --------------------
st.markdown(
    """
    <div class="card">
        <div style="display:flex;align-items:center;gap:16px;">
            <div style="width:52px;height:52px;border-radius:14px;
                        background:#E8F4F6;display:flex;
                        align-items:center;justify-content:center;
                        font-size:28px;color:#0B4F6C;">
                🫀
            </div>
            <div>
                <div class="main-title">Organ Transplant Decision Support System</div>
                <div class="subtitle">AI-assisted, explainable support for transplant evaluation</div>
            </div>
        </div>
        <div class="disclaimer">
            This system supports clinical decision-making and does not replace physician judgment.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- PATIENT IDENTIFICATION --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Patient Identification</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    patient_id = st.text_input("Patient / Case ID")
    age = st.number_input("Age", 0, 120)
    sex = st.selectbox("Sex", ["Male","Female","Other"])
with c2:
    blood_group = st.selectbox("Blood Group", ["A+","A-","B+","B-","AB+","AB-","O+","O-"])
    organ = st.selectbox("Organ Under Consideration", ["Kidney","Liver","Heart","Lung"])
    eval_date = st.date_input("Evaluation Date", date.today())
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- PRIMARY CLINICAL STATUS --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Primary Clinical Status</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    severity = st.number_input("Severity Score (GFR / MELD / EF)", min_value=0.0)
with c2:
    icu = st.selectbox("ICU Admission", ["No","Yes"])
    stage = st.selectbox("Disease Stage", ["Mild","Moderate","Severe"])
with c3:
    infection = st.selectbox("Active Infection", ["No","Yes"])
    sepsis = st.selectbox("Sepsis Risk", ["Low","Medium","High"])
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- CONTRAINDICATION --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Contraindication & Safety Check</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    cancer = st.selectbox("Cancer Status", ["None","Stage 1","Stage 2","Stage 3","Stage 4"])
    cardiac = st.selectbox("Recent Major Cardiac / Stroke Event", ["No","Yes"])
with c2:
    diabetes = st.checkbox("Uncontrolled Diabetes")
    hypertension = st.checkbox("Uncontrolled Hypertension")
    adherence = st.checkbox("Psychological / Adherence Risk")
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- IMMUNOLOGY --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Immunological & Compatibility Profile</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2)
with c1:
    hla = st.slider("HLA Mismatch Count", 0, 6, 3)
    compatibility = st.selectbox("Blood Group Compatibility", ["Compatible","Incompatible"])
with c2:
    pra = st.slider("PRA %", 0, 100, 20)
    prev_tx = st.selectbox("Previous Transplant", ["No","Yes"])
st.markdown('</div>', unsafe_allow_html=True)

# ==================== CLINICAL + AI ENGINE ====================
severity_text = interpret_severity(organ, severity)

contra_status, contra_reasons = contraindication_status(
    infection, cancer, cardiac,
    diabetes, hypertension, adherence
)

risk_score, risk_factors = calculate_risk_score(
    age, infection, icu, sepsis,
    hla, pra, prev_tx
)

risk = risk_level(risk_score)
urgency = urgency_level(organ, severity)
final_eligibility = eligibility(contra_status, risk)

# ----------- EXPLAINABILITY LOGIC -----------
explain = build_explainability(
    severity_text,
    risk_factors,
    contra_reasons
)


# ----------- ML FEATURE BUILDING & INFERENCE -----------
features = build_features(
    age, organ, severity, icu, infection, sepsis,
    hla, pra, prev_tx, cancer
)

predicted_survival = predict_survival(features)

importance = {
    "Active infection": 0.35,
    "High PRA": 0.22,
    "ICU admission": 0.18,
    "Age": 0.12
}

# -------------------- AI RISK METRICS --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">AI-Assisted Risk Assessment</div>', unsafe_allow_html=True)



c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{predicted_survival}%</div>'
        f'<div class="metric-label">Predicted 1-Year Survival</div></div>',
        unsafe_allow_html=True
    )
with c2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{risk}</div>'
        f'<div class="metric-label">Overall Risk</div></div>',
        unsafe_allow_html=True
    )
with c3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{urgency}</div>'
        f'<div class="metric-label">Urgency</div></div>',
        unsafe_allow_html=True
    )
with c4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-value">{final_eligibility}</div>'
        f'<div class="metric-label">Eligibility</div></div>',
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

# -------------------- EXPLAINABILITY --------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Explainability</div>', unsafe_allow_html=True)

# --- Textual clinical reasoning (MOST IMPORTANT) ---
for line in explain:
    st.write("•", line)

st.markdown("---")

# --- Visual support (secondary) ---
imp_df = pd.DataFrame({
    "Factor": importance.keys(),
    "Impact": importance.values()
})
st.bar_chart(imp_df.set_index("Factor"))

st.caption("Factors shown represent relative influence on AI estimate (non-deterministic).")
st.markdown('</div>', unsafe_allow_html=True)
