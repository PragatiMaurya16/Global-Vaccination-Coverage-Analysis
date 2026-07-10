import pandas as pd
from pathlib import Path
import csv

BASE_DIR = Path(__file__).resolve().parent.parent

input_file = BASE_DIR / "cleaned_data" / "vaccine_schedule_cleaned.csv"
output_file = BASE_DIR / "cleaned_data" / "vaccine_schedule_mysql_fixed.csv"

df = pd.read_csv(input_file)

print("Original rows:", len(df))

df.to_csv(
    output_file,
    index=False,
    quoting=csv.QUOTE_ALL,
    lineterminator="\n"
)

print("Fixed CSV created")
print("Rows:", len(df))