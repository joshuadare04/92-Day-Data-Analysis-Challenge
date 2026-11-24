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
print("FLIGHT DATA CONSISTENCY INVESTIGATION")
print("=" * 65)

# 1. Monthly record counts
print("\n1. RECORD COUNTS BY MONTH")
print(df.groupby("month").size())

# 2. Airlines represented each month
print("\n2. UNIQUE AIRLINES BY MONTH")
print(df.groupby("month")["carrier"].nunique())

print("\n3. AIRLINE PRESENCE ACROSS MONTHS")
airline_months = df.groupby("carrier")["month"].nunique()
print(airline_months.sort_values())

# 3. Airport code consistency
print("\n4. AIRPORT CODE LENGTH CHECK")
print("Origin codes not exactly 3 characters:",
      (df["origin"].str.len() != 3).sum())

print("Destination codes not exactly 3 characters:",
      (df["dest"].str.len() != 3).sum())

print("\n5. UNIQUE AIRPORT COUNTS")
print("Unique origin airports:", df["origin"].nunique())
print("Unique destination airports:", df["dest"].nunique())

# 4. Flight number consistency
print("\n6. FLIGHT NUMBER CHECK")
print("Missing flight numbers:", df["flight_number"].isna().sum())
print("Non-positive flight numbers:",
      (df["flight_number"] <= 0).sum())

# 5. Missing or blank identifiers
print("\n7. MISSING IDENTIFIERS")
identifier_columns = [
    "month", "carrier", "flight_number", "origin", "dest"
]

print(df[identifier_columns].isna().sum())

for column in ["carrier", "origin", "dest"]:
    blank_count = (
        df[column].astype("string").str.strip().eq("").sum()
    )
    print(f"Blank {column} values: {blank_count}")

# 6. Duplicate flight-route records
print("\n8. DUPLICATE FLIGHT-ROUTE IDENTIFIERS")

key_columns = [
    "month", "carrier", "flight_number", "origin", "dest"
]

duplicate_keys = df.duplicated(
    subset=key_columns,
    keep=False
)

print("Records involved in duplicate identifiers:",
      duplicate_keys.sum())

if duplicate_keys.any():
    print(df.loc[duplicate_keys, key_columns]
          .sort_values(key_columns)
          .head(20)
          .to_string(index=False))

# 7. Carrier and airport code formats
print("\n9. IDENTIFIER FORMAT CHECK")

print("Carrier codes not exactly 2 characters:",
      (df["carrier"].str.len() != 2).sum())

print("Origin codes containing non-letters:",
      (~df["origin"].str.fullmatch(r"[A-Za-z]{3}")).sum())

print("Destination codes containing non-letters:",
      (~df["dest"].str.fullmatch(r"[A-Za-z]{3}")).sum())

print("\nINVESTIGATION COMPLETED!")