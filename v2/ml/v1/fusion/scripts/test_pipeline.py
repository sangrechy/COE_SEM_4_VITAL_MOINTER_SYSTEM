import joblib
import pandas as pd

from fusion_engine import fusion_engine

# Load Models

ecg_model = joblib.load(
    "../../ecg/models/ecg_rf_multiclass.pkl"
)

stress_model = joblib.load(
    "../../stress/models/stress_rf_model.pkl"
)

# Example ECG Features

ecg_input = pd.DataFrame([
    {
        "RR_INTERVAL": 0.80,
        "PEAK_AMP": 0.90,
        "BEAT_STD": 0.25,
        "BEAT_ENERGY": 17.0
    }
])

# Example Stress Features

stress_input = pd.DataFrame([
    {
        "HEART_RATE": 90,
        "HRV": 0.12,
        "BODY_TEMPERATURE": 36.8,
        "MOTION_LEVEL": 0.8
    }
])

# Predict

ecg_class = int(
    ecg_model.predict(ecg_input)[0]
)

stress_class = int(
    stress_model.predict(stress_input)[0]
)

# Fusion

alerts = fusion_engine(
    ecg_class=ecg_class,
    stress_class=stress_class,
    heart_rate=90,
    spo2=97,
    temperature=36.8,
    motion=0.8
)

print("\nECG CLASS:", ecg_class)
print("STRESS CLASS:", stress_class)

print("\nFINAL ALERTS:")

for alert in alerts:
    print("-", alert)
