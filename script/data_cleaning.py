import pandas as pd
import os
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
CLEANED_DIR = BASE_DIR / "cleaned_data"

CLEANED_DIR.mkdir(exist_ok=True)

# Load datasets
datasets = {
    "coverage": pd.read_excel(DATA_DIR / "coverage-data.xlsx"),
    "incidence": pd.read_excel(DATA_DIR / "incidence-rate-data.xlsx"),
    "reported_cases": pd.read_excel(DATA_DIR / "reported-cases-data.xlsx"),
    "vaccine_introduction": pd.read_excel(DATA_DIR / "vaccine-introduction-data.xlsx"),
    "vaccine_schedule": pd.read_excel(DATA_DIR / "vaccine-schedule-data.xlsx")
}

required_columns = {
    "coverage": ["CODE", "NAME", "YEAR", "ANTIGEN"],
    "incidence": ["CODE", "NAME", "YEAR", "DISEASE"],
    "reported_cases": ["CODE", "NAME", "YEAR", "DISEASE"],
    "vaccine_introduction": ["ISO_3_CODE", "COUNTRYNAME", "YEAR"],
    "vaccine_schedule": ["ISO_3_CODE", "COUNTRYNAME", "YEAR", "VACCINECODE"]
}

print("=" * 70)
print("DATA CLEANING REPORT")
print("=" * 70)

for name, df in datasets.items():

    print(f"\n{name.upper()}")

    original_rows = len(df)

    # Remove duplicates
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()

    # Remove rows with missing values in important columns
    df = df.dropna(subset=required_columns[name])

    # Convert YEAR to integer
    df["YEAR"] = df["YEAR"].astype(int)

    cleaned_rows = len(df)

    print(f"Original Rows      : {original_rows}")
    print(f"Duplicates Removed : {duplicate_count}")
    print(f"Rows After Cleaning: {cleaned_rows}")
    print(f"Rows Removed       : {original_rows - cleaned_rows}")

    # Save cleaned dataset
    output_path = f"../cleaned_data/{name}_cleaned.csv"
    df.to_csv(output_path, index=False)

    print(f"Saved: {output_path}")

print("\nAll cleaned datasets have been saved successfully!")