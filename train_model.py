import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# ---------------- LOAD DATA ----------------
df = pd.read_csv("data/transplant_survival.csv")

# Encode organ type
le = LabelEncoder()
df["organ_encoded"] = le.fit_transform(df["organ"])

# Features & target
X = df[
    [
        "age",
        "organ_encoded",
        "severity",
        "icu",
        "infection",
        "sepsis",
        "hla",
        "pra",
        "prev_tx",
        "cancer",
    ]
]
y = df["survived_1yr"]

# ---------------- SPLIT ----------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------- MODEL ----------------
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=6,
    random_state=42
)

model.fit(X_train, y_train)

# ---------------- EVALUATION ----------------
preds = model.predict(X_test)
acc = accuracy_score(y_test, preds)
print(f"Model accuracy: {acc:.2f}")

# ---------------- SAVE MODEL ----------------
joblib.dump(
    {"model": model, "label_encoder": le},
    "ml/survival_model.pkl"
)

print("✅ Model saved as ml/survival_model.pkl")
