from pathlib import Path
import re

file = Path(
    "v2/ml/v1/stress/results/stress_forest_export.c"
)

text = file.read_text()

text = re.sub(r'\bfeature_(\d+)\b', r'stress_feature_\1', text)
text = re.sub(r'\bthreshold_(\d+)\b', r'stress_threshold_\1', text)
text = re.sub(r'\bleft_(\d+)\b', r'stress_left_\1', text)
text = re.sub(r'\bright_(\d+)\b', r'stress_right_\1', text)
text = re.sub(r'\bvalue_(\d+)\b', r'stress_value_\1', text)

file.write_text(text)

print("DONE")
