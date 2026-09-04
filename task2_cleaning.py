import os 
import numpy as np
import pandas as pd

DATA_PATH  ="data/shipments_train.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH)


print(df.shape)
print(df.duplicated().sum())

# removing duplicates

duplicates_before = df.duplicated().sum()

df = df.drop_duplicates().copy()
print("\nduplicates removed:" ,duplicates_before)
print(df.shape)

# convert data types

df["dispatch_date"] = pd.to_datetime(df["dispatch_date"],errors="coerce")

df["order_value_inr"] = pd.to_numeric(df["order_value_inr"],errors="coerce")


# handle impossible values

negative_distance = (df["distance_km"] < 0).sum()

df.loc[df["distance_km"] < 0, "distance_km"] = np.nan

absurd_weight = (df["weight_kg"]> 20).sum()

df.loc[df["weight_kg"]>20 , "weight_kg"] = np.nan

print("Negative distances: ", negative_distance)
print("Weights: ", absurd_weight)


# standardizing

categorical_columns = [
    "warehouse_id",
    "courier_partner",
    "destination_city",
    "customer_segment",
    "payment_method",
]

for column in categorical_columns:
    df[column] = (df[column].astype("string").str.strip())

df["destination_city"] = (df["destination_city"].str.lower().str.title())

# missing values


numeric_columns = [
    "distance_km",
    "weight_kg",
    "order_value_inr",
    "rainfall_mm",
    "customer_prior_late_deliveries"
]

categorical_columns = [
    "warehouse_id",
    "courier_partner",
    "destination_city",
    "customer_segment",
    "payment_method"
]

# Numeric columns:
# Fill missing values with the median
for column in numeric_columns:
    median_value = df[column].median()
    df[column] = df[column].fillna(median_value)

# Categorical columns:
# Fill missing values with the most frequent value
for column in categorical_columns:
    mode_value = df[column].mode(dropna=True)

    if len(mode_value) > 0:
        fill_value = mode_value.iloc[0]
    else:
        fill_value = "Unknown"

    df[column] = df[column].fillna(fill_value)

# Check remaining missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# day of week
df["dispatch_dayofweek"] = (df["dispatch_date"].dt.dayofweek)

# day of month
df["dispatch_month"] = (df["dispatch_date"].dt.month)

# distance per promised day
df["distance_per_promised_day"] = (df["distance_km"]/df["promised_days"].replace(0,np.nan))

# late dispatch flag

df["late_dispatch_flag"] = (df["dispatch_hour"] >= 18).astype(int)

# heavy parcel flag 
df["heavy_parcel_flag"] = (df["weight_kg"] >= 5).astype(int)

new_features = [
    "dispatch_dayofweek",
    "dispatch_month",
    "distance_per_promised_day",
    "late_dispatch_flag",
    "heavy_parcel_flag"
]

print("\nNew features: ")
for feature in new_features:
    print("-", feature)

cleaned_path = os.path.join(OUTPUT_DIR, "cleaned_shipment_train.csv")

df.to_csv(cleaned_path, index=False)

print("\nCleaned dataset saved to: ")
print(cleaned_path)