import pickle
import numpy as np
import pandas as pd
from pathlib import Path

DATASET = Path("../../../../../dataset/wesad_raw/WESAD")

rows = []

subjects = sorted(
    [x for x in DATASET.iterdir() if x.is_dir()]
)

print("Subjects Found:", len(subjects))

for subject in subjects:

    pkl_file = subject / f"{subject.name}.pkl"

    try:

        with open(pkl_file, "rb") as f:
            data = pickle.load(f, encoding="latin1")

        labels = data["label"]

        ecg = data["signal"]["chest"]["ECG"].flatten()
        temp = data["signal"]["chest"]["Temp"].flatten()
        acc = data["signal"]["chest"]["ACC"]

        WINDOW = 7000

        for start in range(0, len(labels) - WINDOW, WINDOW):

            end = start + WINDOW

            label = int(labels[start])

            if label not in [1, 2, 3, 4]:
                continue

            ecg_seg = ecg[start:end]
            temp_seg = temp[start:end]
            acc_seg = acc[start:end]

            heart_rate = np.mean(np.abs(ecg_seg))

            hrv = np.std(ecg_seg)

            body_temp = np.mean(temp_seg)

            motion_level = np.mean(
                np.sqrt(
                    acc_seg[:, 0]**2 +
                    acc_seg[:, 1]**2 +
                    acc_seg[:, 2]**2
                )
            )

            mapped_label = {
                1: 0,   # BASELINE
                2: 1,   # STRESS
                3: 2,   # AMUSEMENT
                4: 3    # MEDITATION
            }[label]

            rows.append([
                heart_rate,
                hrv,
                body_temp,
                motion_level,
                mapped_label
            ])

        print("Processed:", subject.name)

    except Exception as e:
        print("Skipped:", subject.name, e)

df = pd.DataFrame(
    rows,
    columns=[
        "HEART_RATE",
        "HRV",
        "BODY_TEMPERATURE",
        "MOTION_LEVEL",
        "LABEL"
    ]
)

df.to_csv(
    "../processed_data/stress_features.csv",
    index=False
)

print("\nDataset Created")
print(df.head())
print("\nSamples:", len(df))
print("\nSaved: ../processed_data/stress_features.csv")
