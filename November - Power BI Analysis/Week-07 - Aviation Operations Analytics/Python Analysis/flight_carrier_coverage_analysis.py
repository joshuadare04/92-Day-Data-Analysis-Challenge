import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

csv_files = sorted(source_dir.glob("*.csv"))

df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in csv_files],
    ignore_index=True
)

print("=" * 65)
print("AIRLINE MONTHLY COVERAGE ANALYSIS")
print("=" * 65)

# 1. Airline presence by month
print("\n1. AIRLINE PRESENCE MATRIX")

coverage = pd.crosstab(df["carrier"], df["month"])

# Convert record counts into presence indicators
presence = (coverage > 0).astype(int)

print(presence.to_string())

# 2. Months represented by each airline
print("\n2. MONTHLY COVERAGE SUMMARY")

summary = pd.DataFrame({
    "months_present": presence.sum(axis=1),
    "months_absent": len(presence.columns) - presence.sum(axis=1),
    "records": df.groupby("carrier").size()
})

print(summary.sort_values("months_present").to_string())

# 3. Identify missing months for each airline
print("\n3. MISSING MONTHS BY AIRLINE")

all_months = sorted(df["month"].unique())

for carrier in sorted(df["carrier"].unique()):
    present_months = df.loc[
        df["carrier"] == carrier, "month"
    ].unique()

    missing_months = sorted(
        set(all_months) - set(present_months)
    )

    if missing_months:
        print(f"{carrier}: {', '.join(missing_months)}")

# 4. Monthly record counts for HA and NK
print("\n4. HA AND NK MONTHLY RECORD COUNTS")

selected = df[df["carrier"].isin(["HA", "NK"])]

print(
    selected.groupby(["carrier", "month"])
    .size()
    .unstack(fill_value=0)
    .to_string()
)

# 5. Overall airline record distribution
print("\n5. AIRLINE RECORD DISTRIBUTION (%)")

airline_records = df.groupby("carrier").size()

airline_percentage = (
    airline_records / len(df) * 100
).round(2)

print(
    pd.DataFrame({
        "records": airline_records,
        "percentage": airline_percentage
    }).sort_values("records", ascending=False)
)

print("\nANALYSIS COMPLETED!")