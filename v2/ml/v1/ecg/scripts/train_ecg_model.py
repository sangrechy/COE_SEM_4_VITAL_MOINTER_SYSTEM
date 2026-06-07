import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=25,
    max_depth=12,
    min_samples_leaf=5,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, pred))

print("\nClassification Report:")
print(classification_report(y_test, pred))

joblib.dump(
    model,
    "../models/ecg_rf_multiclass.pkl"
)

print("\nModel Saved:")
print("../models/ecg_rf_multiclass.pkl")
