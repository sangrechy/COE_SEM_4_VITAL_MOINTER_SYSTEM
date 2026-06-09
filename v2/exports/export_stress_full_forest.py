import joblib
import os
import numpy as np

MODEL_PATH = "v2/ml/v1/stress/models/stress_rf_model.pkl"
OUTPUT_PATH = "v2/ml/v1/stress/results/stress_forest_export.c"

model = joblib.load(MODEL_PATH)

with open(OUTPUT_PATH, "w") as f:

    f.write("// AUTO GENERATED STRESS RANDOM FOREST\n\n")
    f.write(f"#define STRESS_TREE_COUNT {len(model.estimators_)}\n\n")

    for idx, estimator in enumerate(model.estimators_):

        tree = estimator.tree_

        f.write(f"// TREE {idx}\n\n")

        f.write(f"const int feature_{idx}[] = {{")
        f.write(",".join(map(str, tree.feature.tolist())))
        f.write("};\n\n")

        f.write(f"const float threshold_{idx}[] = {{")
        f.write(",".join(map(str, tree.threshold.tolist())))
        f.write("};\n\n")

        f.write(f"const int left_{idx}[] = {{")
        f.write(",".join(map(str, tree.children_left.tolist())))
        f.write("};\n\n")

        f.write(f"const int right_{idx}[] = {{")
        f.write(",".join(map(str, tree.children_right.tolist())))
        f.write("};\n\n")

        values = tree.value

        classes = []

        for node in values:
            cls = int(np.argmax(node[0]))
            classes.append(str(cls))

        f.write(f"const int value_{idx}[] = {{")
        f.write(",".join(classes))
        f.write("};\n\n")

print("=================================")
print("STRESS Forest Export Complete")
print("=================================")
print("Trees:", len(model.estimators_))
print("Output:", OUTPUT_PATH)
print("Size:", round(os.path.getsize(OUTPUT_PATH)/(1024*1024), 2), "MB")
