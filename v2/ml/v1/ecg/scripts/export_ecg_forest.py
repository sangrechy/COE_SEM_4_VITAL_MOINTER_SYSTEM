import joblib

model = joblib.load("../models/ecg_rf_multiclass.pkl")

print("Trees:", len(model.estimators_))

total_nodes = 0

for i, tree in enumerate(model.estimators_):

    node_count = tree.tree_.node_count
    depth = tree.tree_.max_depth

    total_nodes += node_count

    print(
        f"Tree {i}: "
        f"Depth={depth} "
        f"Nodes={node_count}"
    )

print("\nTotal Nodes:", total_nodes)

with open("../results/ecg_forest_summary.txt", "w") as f:

    f.write(
        f"Trees: {len(model.estimators_)}\n"
    )

    f.write(
        f"Total Nodes: {total_nodes}\n"
    )

print(
    "\nSaved:"
    " ../results/ecg_forest_summary.txt"
)
