import joblib

model = joblib.load("../models/ecg_rf_multiclass.pkl")

tree = model.estimators_[0].tree_

print("Nodes:", tree.node_count)
print("Depth:", tree.max_depth)

print("\nchildren_left")
print(tree.children_left[:20])

print("\nchildren_right")
print(tree.children_right[:20])

print("\nfeature")
print(tree.feature[:20])

print("\nthreshold")
print(tree.threshold[:20])
