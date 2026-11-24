import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

csv_files = sorted(source_dir.glob("*.csv"))

df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in csv_files],
    ignore_index=True
)

delay_columns = ["arr_delay_mean", "arr_delay_median"]

print("=" * 65)
print("EXTREME ARRIVAL DELAY INVESTIGATION")
print("=" * 65)

# 1. Delay distribution
print("\n1. ARRIVAL DELAY STATISTICS")
print(df[delay_columns].describe().round(2))

# 2. Positive delay distribution
print("\n2. POSITIVE MEAN ARRIVAL DELAYS")
print("Above 60 minutes:",
      (df["arr_delay_mean"] > 60).sum())
print("Above 120 minutes:",
      (df["arr_delay_mean"] > 120).sum())
print("Above 300 minutes:",
      (df["arr_delay_mean"] > 300).sum())
print("Above 600 minutes:",
      (df["arr_delay_mean"] > 600).sum())

# 3. Highest mean arrival delays
print("\n3. TOP 20 HIGHEST MEAN ARRIVAL DELAYS")
print(
    df.nlargest(20, "arr_delay_mean")[[
        "month", "carrier", "flight_number",
        "origin", "dest", "flights",
        "cancelled", "diverted", "on_time",
        "late_30", "arr_delay_mean", "arr_delay_median"
    ]].to_string(index=False)
)

# 4. Extreme delays by airline
print("\n4. EXTREME DELAYS BY AIRLINE (ABOVE 120 MINUTES)")
print(
    df[df["arr_delay_mean"] > 120]
    .groupby("carrier")
    .size()
    .sort_values(ascending=False)
)

# 5. Extreme delays by month
print("\n5. EXTREME DELAYS BY MONTH (ABOVE 120 MINUTES)")
print(
    df[df["arr_delay_mean"] > 120]
    .groupby("month")
    .size()
)

# 6. Compare mean and median for extreme records
print("\n6. EXTREME RECORDS: MEAN VS MEDIAN")
extreme = df[df["arr_delay_mean"] > 120].copy()
extreme["mean_median_difference"] = (
    extreme["arr_delay_mean"] - extreme["arr_delay_median"]
)

print(
    extreme[[
        "carrier", "flight_number", "origin", "dest",
        "flights", "arr_delay_mean",
        "arr_delay_median", "mean_median_difference"
    ]].head(15).to_string(index=False)
)

print("\nINVESTIGATION COMPLETED!")