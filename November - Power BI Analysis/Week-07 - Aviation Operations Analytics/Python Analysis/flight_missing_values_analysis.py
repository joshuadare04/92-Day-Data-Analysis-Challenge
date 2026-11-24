import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

csv_files = sorted(source_dir.glob("*.csv"))

df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in csv_files],
    ignore_index=True
)

print("=" * 60)
print("MISSING ARRIVAL DELAY VALUES INVESTIGATION")
print("=" * 60)

# 1. Overall missing values
print("\n1. OVERALL MISSING VALUES")
print(df[["arr_delay_mean", "arr_delay_median"]].isnull().sum())

# 2. Missing values by flight count
print("\n2. MISSING VALUES BY NUMBER OF FLIGHTS")
print(
    df[df["arr_delay_mean"].isnull()]
    .groupby("flights")
    .size()
    .sort_values(ascending=False)
)

# 3. Missing values by airline
print("\n3. MISSING VALUES BY AIRLINE")
print(
    df[df["arr_delay_mean"].isnull()]
    .groupby("carrier")
    .size()
    .sort_values(ascending=False)
)

# 4. Missing values by month
print("\n4. MISSING VALUES BY MONTH")
print(
    df[df["arr_delay_mean"].isnull()]
    .groupby("month")
    .size()
)

# 5. Sample missing records
print("\n5. SAMPLE RECORDS WITH MISSING DELAY VALUES")
print(
    df[df["arr_delay_mean"].isnull()][[
        "month", "carrier", "flight_number",
        "origin", "dest", "flights",
        "cancelled", "diverted", "on_time", "late_30"
    ]].head(15).to_string(index=False)
)

# 6. Compare flight counts
print("\n6. FLIGHT COUNT COMPARISON")
print("Average flights where delay mean is missing:",
      df.loc[df["arr_delay_mean"].isnull(), "flights"].mean())

print("Average flights where delay mean is available:",
      df.loc[df["arr_delay_mean"].notnull(), "flights"].mean())

print("\nINVESTIGATION COMPLETED!")