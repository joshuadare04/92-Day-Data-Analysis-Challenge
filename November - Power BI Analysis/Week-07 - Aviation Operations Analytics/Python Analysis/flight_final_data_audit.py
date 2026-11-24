import pandas as pd
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"
output_dir = Path(__file__).resolve().parent

csv_files = sorted(source_dir.glob("*.csv"))

df = pd.concat(
    [pd.read_csv(file, low_memory=False) for file in csv_files],
    ignore_index=True
)

# Calculate flight outcomes
df["operated_flights"] = (
    df["flights"] - df["cancelled"] - df["diverted"]
)

df["other_arrival_outcomes"] = (
    df["operated_flights"] - df["on_time"] - df["late_30"]
)

# Collect audit findings
audit = {
    "Total monthly files": len(csv_files),
    "Total records": len(df),
    "Total columns": len(df.columns) - 2,
    "Duplicate rows": int(df.duplicated().sum()),
    "Duplicate flight-route identifiers": int(
        df.duplicated(
            subset=["month", "carrier", "flight_number", "origin", "dest"]
        ).sum()
    ),
    "Total missing values": int(df.isna().sum().sum()),
    "Missing mean delay values": int(df["arr_delay_mean"].isna().sum()),
    "Missing median delay values": int(df["arr_delay_median"].isna().sum()),
    "Negative flight counts": int((df["flights"] < 0).sum()),
    "Negative cancellation counts": int((df["cancelled"] < 0).sum()),
    "Negative diversion counts": int((df["diverted"] < 0).sum()),
    "Negative on-time counts": int((df["on_time"] < 0).sum()),
    "Negative late counts": int((df["late_30"] < 0).sum()),
    "Unique airlines": int(df["carrier"].nunique()),
    "Unique origin airports": int(df["origin"].nunique()),
    "Unique destination airports": int(df["dest"].nunique()),
    "Scheduled flights": int(df["flights"].sum()),
    "Cancelled flights": int(df["cancelled"].sum()),
    "Diverted flights": int(df["diverted"].sum()),
    "Operated flights": int(df["operated_flights"].sum()),
    "On-time flights": int(df["on_time"].sum()),
    "Flights delayed over 30 minutes": int(df["late_30"].sum()),
    "Other arrival outcomes": int(df["other_arrival_outcomes"].sum()),
    "Records with mean delay above 120 minutes": int(
        (df["arr_delay_mean"] > 120).sum()
    ),
    "Records with mean delay above 600 minutes": int(
        (df["arr_delay_mean"] > 600).sum()
    ),
    "Maximum mean arrival delay": float(df["arr_delay_mean"].max()),
    "Airlines present in all months": int(
        (df.groupby("carrier")["month"].nunique() == df["month"].nunique()).sum()
    ),
    "Airlines with incomplete monthly coverage": int(
        (df.groupby("carrier")["month"].nunique() < df["month"].nunique()).sum()
    )
}

print("=" * 65)
print("FINAL AVIATION DATA QUALITY AUDIT")
print("=" * 65)

for metric, value in audit.items():
    print(f"{metric}: {value}")

# Airline coverage summary
print("\n" + "=" * 65)
print("AIRLINE COVERAGE SUMMARY")
print("=" * 65)

coverage = df.groupby("carrier").agg(
    records=("carrier", "size"),
    months_present=("month", "nunique")
)

coverage["months_absent"] = (
    df["month"].nunique() - coverage["months_present"]
)

print(coverage.sort_values("months_present").to_string())

# Save audit summary
audit_df = pd.DataFrame(
    list(audit.items()),
    columns=["Metric", "Value"]
)

output_file = output_dir / "flight_final_data_audit_summary.csv"
audit_df.to_csv(output_file, index=False)

print("\n" + "=" * 65)
print("FINAL AUDIT COMPLETED!")
print(f"Audit summary saved to: {output_file}")
print("=" * 65)