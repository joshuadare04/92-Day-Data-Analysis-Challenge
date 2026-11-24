import pandas as pd
from pathlib import Path

# Project directories
project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

# Locate CSV files
csv_files = sorted(source_dir.glob("*.csv"))

print("=" * 65)
print("AVIATION OPERATIONS ANALYTICS")
print("DETAILED DATA EXPLORATION")
print("=" * 65)

# Load and combine datasets
dataframes = []

for file in csv_files:
    df = pd.read_csv(file, low_memory=False)
    dataframes.append(df)

flights_df = pd.concat(dataframes, ignore_index=True)

print(f"\nTotal Records: {len(flights_df):,}")
print(f"Total Columns: {len(flights_df.columns)}")

# 1. Inspect sample records
print("\n1. FIRST 10 RECORDS")
print(flights_df.head(10).to_string(index=False))

# 2. Inspect random records
print("\n2. RANDOM 5 RECORDS")
print(flights_df.sample(5, random_state=42).to_string(index=False))

# 3. Check reporting months
print("\n3. REPORTING MONTHS")
print(flights_df["month"].value_counts().sort_index())

# 4. Check unique airlines
print("\n4. UNIQUE AIRLINES")
print(f"Total Airlines: {flights_df['carrier'].nunique()}")
print(flights_df["carrier"].value_counts())

# 5. Check airport coverage
print("\n5. AIRPORT COVERAGE")
print(f"Unique Origin Airports: {flights_df['origin'].nunique()}")
print(f"Unique Destination Airports: {flights_df['dest'].nunique()}")

# 6. Numerical summary
print("\n6. NUMERICAL SUMMARY")
print(flights_df.describe().round(2).to_string())

# 7. Check flight count consistency
print("\n7. FLIGHT COUNT CHECKS")

print("Flights with zero recorded flights:")
print((flights_df["flights"] == 0).sum())

print("\nCancelled flights exceeding total flights:")
print((flights_df["cancelled"] > flights_df["flights"]).sum())

print("\nDiverted flights exceeding total flights:")
print((flights_df["diverted"] > flights_df["flights"]).sum())

print("\nOn-time flights exceeding total flights:")
print((flights_df["on_time"] > flights_df["flights"]).sum())

# 8. Missing delay statistics
print("\n8. MISSING DELAY STATISTICS")
print(flights_df[
    flights_df["arr_delay_mean"].isna()
][["month", "carrier", "flight_number", "origin", "dest", "flights"]].head(10))

print("\nEXPLORATION COMPLETED!")