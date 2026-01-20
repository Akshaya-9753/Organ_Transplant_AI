import numpy as np
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "survival_model.pkl"

MODEL = joblib.load(MODEL_PATH)

def predict_survival(features: dict) -> int:
    """
    features: dict from build_features()
    returns: survival probability percentage
    """
    ordered_features = np.array([[
        features["age"],
        features["organ"],
        features["severity"],
        features["icu"],
        features["infection"],
        features["sepsis"],
        features["hla"],
        features["pra"],
        features["prev_tx"],
        features["cancer"]
    ]], dtype=float)

    prob = MODEL.predict_proba(ordered_features)[0][1]
    return int(round(prob * 100))
