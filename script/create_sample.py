import pandas as pd
from pathlib import Path

# Project path
BASE_DIR = Path(__file__).resolve().parent.parent

# File locations
input_file = BASE_DIR / "cleaned_data" / "coverage_cleaned.csv"
output_file = BASE_DIR / "cleaned_data" / "coverage_sample.csv"

# Load cleaned coverage data
coverage = pd.read_csv(input_file)

print("Original Shape:")
print(coverage.shape)

# Take 50,000 rows
coverage_sample = coverage.sample(
    n=50000,
    random_state=42
)

# Save sample file
coverage_sample.to_csv(
    output_file,
    index=False
)

print("\nSample Created Successfully!")
print("Sample Shape:")
print(coverage_sample.shape)

print("\nSaved at:")
print(output_file)