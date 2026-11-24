import pandas as pd
from pathlib import Path

# Project directories
project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

# Load and combine datasets
csv_files = sorted(source_dir.glob("*.csv"))

df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in csv_files],
    ignore_index=True
)

# Calculate unaccounted flights
df["recorded_outcomes"] = (
    df["cancelled"] +
    df["diverted"] +
    df["on_time"] +
    df["late_30"]
)

df["unaccounted_flights"] = (
    df["flights"] - df["recorded_outcomes"]
)

print("=" * 60)
print("FLIGHT OUTCOME INVESTIGATION")
print("=" * 60)

# 1. Inspect records with unaccounted flights
print("\n1. SAMPLE RECORDS WITH UNACCOUNTED FLIGHTS")

print(
    df[df["unaccounted_flights"] > 0][
        [
            "month", "carrier", "flight_number",
            "origin", "dest", "flights",
            "cancelled", "diverted",
            "on_time", "late_30",
            "unaccounted_flights"
        ]
    ].head(15).to_string(index=False)
)

# 2. Average unaccounted flights by airline
print("\n2. UNACCOUNTED FLIGHTS BY AIRLINE")

print(
    df.groupby("carrier")["unaccounted_flights"]
    .agg(["sum", "mean", "max"])
    .sort_values("sum", ascending=False)
    .round(2)
)

# 3. Unaccounted flights by month
print("\n3. UNACCOUNTED FLIGHTS BY MONTH")

print(
    df.groupby("month")["unaccounted_flights"]
    .sum()
)

# 4. Check whether outcome categories overlap
print("\n4. OUTCOME CATEGORY CHECK")

print("Cancelled and diverted both greater than zero:")
print(((df["cancelled"] > 0) & (df["diverted"] > 0)).sum())

print("On-time and late_30 both greater than zero:")
print(((df["on_time"] > 0) & (df["late_30"] > 0)).sum())

print("\nINVESTIGATION COMPLETED!")