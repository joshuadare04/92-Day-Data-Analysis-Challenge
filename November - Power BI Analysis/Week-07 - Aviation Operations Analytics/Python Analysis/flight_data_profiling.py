import pandas as pd
from pathlib import Path

# Define project directories
project_dir = Path(__file__).resolve().parent.parent
source_dir = project_dir / "Source Data"

# Locate all CSV files
csv_files = sorted(source_dir.glob("*.csv"))

print("=" * 60)
print("AVIATION OPERATIONS ANALYTICS")
print("INITIAL DATASET PROFILING")
print("=" * 60)

print(f"\nTotal CSV files found: {len(csv_files)}")

# Store profiling results
profiling_results = []

# Inspect each CSV file
for file in csv_files:

    print("\n" + "=" * 60)
    print(f"FILE: {file.name}")
    print("=" * 60)

    try:
        df = pd.read_csv(file, low_memory=False)

    except UnicodeDecodeError:
        df = pd.read_csv(file, encoding="latin1", low_memory=False)

    # Basic information
    rows, columns = df.shape

    print(f"Number of rows: {rows:,}")
    print(f"Number of columns: {columns}")
    print(f"Duplicate rows: {df.duplicated().sum():,}")
    print(f"Missing values: {df.isnull().sum().sum():,}")

    print("\nCOLUMN NAMES:")
    print(df.columns.tolist())

    print("\nDATA TYPES:")
    print(df.dtypes)

    print("\nMISSING VALUES BY COLUMN:")
    print(df.isnull().sum())

    # Save file-level summary
    profiling_results.append({
        "File Name": file.name,
        "Rows": rows,
        "Columns": columns,
        "Duplicate Rows": df.duplicated().sum(),
        "Missing Values": df.isnull().sum().sum()
    })

# Create summary report
summary = pd.DataFrame(profiling_results)

output_file = project_dir / "Python Analysis" / "dataset_profiling_summary.csv"

summary.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("PROFILING COMPLETED!")
print("=" * 60)

print(summary.to_string(index=False))
print(f"\nSummary saved to: {output_file}")