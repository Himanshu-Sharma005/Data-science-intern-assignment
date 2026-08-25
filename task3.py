import pandas as pd

df = pd.read_csv("outputs/cleaned_shipment_train.csv")

y= df["is_late"]

baseline_prediction = 0

basline_accuracy =  (y == baseline_prediction).mean()

print("Total shipments:", len(y))
print("Actual late shipments:" , y.sum())
print("Actual on time shipments:" , (y==0).sum())

print("Baseline accuracy:", round(basline_accuracy,4))

print("Baseline accuracy (%):", round(basline_accuracy * 100, 2),"%")