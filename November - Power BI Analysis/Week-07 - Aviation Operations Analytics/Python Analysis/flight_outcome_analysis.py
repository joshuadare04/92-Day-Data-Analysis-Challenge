import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

csv_files = sorted(source_dir.glob("*.csv"))

df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in csv_files],
    ignore_index=True
)

# Calculate flights that actually operated
df["operated_flights"] = (
    df["flights"] - df["cancelled"] - df["diverted"]
)

# Calculate flights outside the two recorded arrival categories
df["other_arrival_outcomes"] = (
    df["operated_flights"] - df["on_time"] - df["late_30"]
)

print("=" * 60)
print("FLIGHT ARRIVAL OUTCOME ANALYSIS")
print("=" * 60)

print("\n1. OVERALL FLIGHT TOTALS")
print("Scheduled flights:", df["flights"].sum())
print("Cancelled flights:", df["cancelled"].sum())
print("Diverted flights:", df["diverted"].sum())
print("Operated flights:", df["operated_flights"].sum())
print("On-time flights:", df["on_time"].sum())
print("Flights delayed over 30 minutes:", df["late_30"].sum())
print("Other arrival outcomes:", df["other_arrival_outcomes"].sum())

print("\n2. OTHER ARRIVAL OUTCOMES BY AIRLINE")
print(
    df.groupby("carrier")["other_arrival_outcomes"]
    .sum()
    .sort_values(ascending=False)
)

print("\n3. OTHER ARRIVAL OUTCOMES BY MONTH")
print(
    df.groupby("month")["other_arrival_outcomes"]
    .sum()
)

print("\n4. CHECK FOR NEGATIVE RESULTS")
print(
    "Records with negative other arrival outcomes:",
    (df["other_arrival_outcomes"] < 0).sum()
)

print("\nANALYSIS COMPLETED!")