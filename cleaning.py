import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/shipments_train.csv")

# print(df.shape)
# print(df.dtypes)
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df["is_late"].value_counts())
# print(df["is_late"].value_counts(normalize=True))

# # basic
# print(df.describe())

# late rate by courier

# courier_late_rate = (df.groupby("courier_partner")["is_late"].mean().sort_values(ascending=False))

# plt.figure(figsize=(8,5))
# courier_late_rate.plot(kind="bar")

# plt.title("Late rate by courier partner")
# plt.xlabel("courier partner")
# plt.ylabel("late rate")
# plt.xticks(rotation=30, ha="right")
# plt.tight_layout()

# plt.show()

# late rate by promised days


# promised_late_rate=(df.groupby("promised_days")["is_late"].mean())

# plt.figure(figsize=(7,5))

# promised_late_rate.plot(kind="bar")

# plt.title("Late rate by promised deliverity days")
# plt.xlabel("Promised days")
# plt.ylabel("late rate")
# plt.xticks(rotation=0)
# plt.tight_layout()

# plt.show()

# late vs on-time

# plt.figure(figsize=(8,5))
# plt.hist(df[df["is_late"] == 0]["distance_km"].dropna(),bins=30,alpha=0.6,label="on time")

# plt.hist(df[df["is_late"]== 1]["distance_km"].dropna(),bins=30,alpha=0.6,label="Late")

# plt.title("Distance distribution : late vs on time")
# plt.xlabel("distance")
# plt.ylabel("number of shipments")
# plt.legend()
# plt.tight_layout()

# plt.show()

# late rate by month of dispatch

df["dispatch_date"] = pd.to_datetime(df["dispatch_date"])
df["dispatch_month"] = df["dispatch_date"].dt.month

monthly_late_rate = (df.groupby("dispatch_month")["is_late"].mean())

plt.figure(figsize=(8,5))
monthly_late_rate.plot(marker="o")

plt.title("Late rate by dispatch month")
plt.xlabel("Month")
plt.ylabel("Late rate")
plt.xticks(range(1,13))
plt.tight_layout()
plt.show()