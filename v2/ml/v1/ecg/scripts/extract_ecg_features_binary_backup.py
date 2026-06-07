import wfdb
import pandas as pd
import numpy as np
from pathlib import Path

# MIT-BIH dataset location
DATASET = Path(
    "../../../../../dataset/mitbih_raw/physionet.org/files/mitdb/1.0.0"
)

print("Dataset Exists:", DATASET.exists())

# Only keep actual MIT-BIH records (100.dat, 101.dat, etc.)
records = sorted(
    [
        f.stem
        for f in DATASET.glob("*.dat")
        if len(f.stem) == 3 and f.stem.isdigit()
    ]
)

print("MIT-BIH Records Found:", len(records))

rows = []

for rec in records:

    try:
        signal, fields = wfdb.rdsamp(str(DATASET / rec))
        ann = wfdb.rdann(str(DATASET / rec), "atr")

        ecg = signal[:, 0]
        peaks = ann.sample

        for i in range(1, len(peaks) - 1):

            rr = (peaks[i] - peaks[i - 1]) / fields["fs"]

            start = max(0, peaks[i] - 50)
            end = min(len(ecg), peaks[i] + 50)

            beat = ecg[start:end]

            if len(beat) < 20:
                continue

            peak_amp = np.max(np.abs(beat))
            beat_std = np.std(beat)
            beat_energy = np.sum(beat ** 2)

            symbol = ann.symbol[i]

            # Normal beat = 0
            # Any abnormal beat = 1
            label = 0 if symbol == "N" else 1

            rows.append([
                rr,
                peak_amp,
                beat_std,
                beat_energy,
                label
            ])

        print("Processed:", rec)

    except Exception as e:
        print("Skipped:", rec, e)

df = pd.DataFrame(
    rows,
    columns=[
        "RR_INTERVAL",
        "PEAK_AMP",
        "BEAT_STD",
        "BEAT_ENERGY",
        "LABEL"
    ]
)

output_file = "../processed_data/ecg_features.csv"

df.to_csv(output_file, index=False)

print("\nDataset Created")
print(df.head())
print("\nSamples:", len(df))
print("Saved:", output_file)
