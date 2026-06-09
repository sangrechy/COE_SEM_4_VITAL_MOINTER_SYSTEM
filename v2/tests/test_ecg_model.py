import joblib

model = joblib.load(
    "v2/ml/v1/ecg/models/ecg_rf_multiclass.pkl"
)

CLASS_NAMES = {
    0: "NORMAL",
    1: "PVC",
    2: "PAC",
    3: "LBBB",
    4: "RBBB",
    5: "OTHER_ABNORMAL"
}

test_cases = [

    [60.0, 0.20, 0.10, 0.30],
    [75.0, 0.40, 0.20, 0.60],
    [90.0, 0.50, 0.30, 0.80],
    [110.0, 0.70, 0.50, 1.20],
    [130.0, 0.90, 0.80, 1.50]

]

for i, case in enumerate(test_cases, start=1):

    pred = model.predict([case])[0]

    print()
    print("=" * 50)
    print("PATIENT", i)
    print("=" * 50)

    print("RR_INTERVAL :", case[0])
    print("PEAK_AMP    :", case[1])
    print("BEAT_STD    :", case[2])
    print("BEAT_ENERGY :", case[3])

    print()
    print("ECG DIAGNOSIS")
    print("-------------")
    print(CLASS_NAMES[pred])

    print()
