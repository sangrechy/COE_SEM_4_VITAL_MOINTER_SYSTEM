import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load dataset
df = pd.read_csv("../processed_data/ecg_features.csv")

X = df[
    [
        "RR_INTERVAL",
        "PEAK_AMP",
        "BEAT_STD",
        "BEAT_ENERGY"
    ]
]

y = df["LABEL"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Predict
pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))

# Save model
joblib.dump(
    model,
    "../models/ecg_rf_model.pkl"
)

print("\nModel Saved:")
print("../models/ecg_rf_model.pkl")
