import joblib

model = joblib.load(
    "v2/ml/v1/stress/models/stress_rf_model.pkl"
)

print("CLASSES:")
print(model.classes_)
