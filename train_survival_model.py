import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load synthetic data
df = pd.read_csv("data/transplant_survival.csv")

# Encode organ
df["organ"] = df["organ"].map({
    "Kidney": 0,
    "Liver": 1,
    "Heart": 2,
    "Lung": 3
})

X = df.drop(columns=["survived_1yr"])
y = df["survived_1yr"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

joblib.dump(model, "ml/survival_model.pkl")

print("✅ Model trained and saved successfully")
