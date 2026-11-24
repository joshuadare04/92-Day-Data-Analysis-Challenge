import pandas as pd
from pathlib import Path

# Project directories
project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

# Load and combine all monthly files
csv_files = sorted(source_dir.glob("*.csv"))

dataframes = [
    pd.read_csv(file, low_memory=False)
    for file in csv_files
]

df = pd.concat(dataframes, ignore_index=True)

print("=" * 65)
print("AVIATION OPERATIONS ANALYTICS")
print("DATA QUALITY INVESTIGATION")
print("=" * 65)

# 1. Flight outcome reconciliation
print("\n1. FLIGHT OUTCOME RECONCILIATION")

df["recorded_outcomes"] = (
    df["cancelled"] +
    df["diverted"] +
    df["on_time"] +
    df["late_30"]
)

df["outcome_difference"] = (
    df["flights"] - df["recorded_outcomes"]
)

print("Records where recorded outcomes differ from total flights:")
print((df["outcome_difference"] != 0).sum())

print("\nDifference distribution:")
print(df["outcome_difference"].value_counts().sort_index())

# 2. Negative values
print("\n2. NEGATIVE NUMERICAL VALUES")

numeric_columns = [
    "flights", "cancelled", "diverted",
    "on_time", "late_30",
    "arr_delay_mean", "arr_delay_median"
]

for column in numeric_columns:
    print(f"{column}: {(df[column] < 0).sum():,}")

# 3. Extreme arrival delays
print("\n3. EXTREME ARRIVAL DELAYS")

print("Highest average arrival delays:")
print(
    df.nlargest(10, "arr_delay_mean")[
        ["month", "carrier", "flight_number",
         "origin", "dest", "flights", "arr_delay_mean"]
    ].to_string(index=False)
)

# 4. Missing delay statistics by airline
print("\n4. MISSING DELAY STATISTICS BY AIRLINE")

missing_by_carrier = (
    df.groupby("carrier")
    .agg(
        Total_Records=("carrier", "size"),
        Missing_Mean=("arr_delay_mean", "count")
    )
)

missing_by_carrier["Missing_Mean"] = (
    missing_by_carrier["Total_Records"] -
    missing_by_carrier["Missing_Mean"]
)

missing_by_carrier["Missing_Percentage"] = (
    missing_by_carrier["Missing_Mean"] /
    missing_by_carrier["Total_Records"] * 100
)

print(missing_by_carrier.sort_values(
    "Missing_Mean", ascending=False
).round(2).to_string())

# 5. Flight outcome totals
print("\n5. OVERALL FLIGHT COUNTS")

print(df[
    ["flights", "cancelled", "diverted", "on_time", "late_30"]
].sum().to_string())

print("\nDATA QUALITY INVESTIGATION COMPLETED!")