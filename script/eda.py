import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ------------------------------------
# Project Paths
# ------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
CLEANED_DATA = BASE_DIR / "cleaned_data"

# ------------------------------------
# Load Dataset
# ------------------------------------
coverage = pd.read_csv(CLEANED_DATA / "coverage_cleaned.csv")

print("=" * 60)
print("COVERAGE DATASET")
print("=" * 60)

print("\nShape:")
print(coverage.shape)

print("\nColumns:")
print(coverage.columns.tolist())

print("\nData Types:")
print(coverage.dtypes)

print("\nMissing Values:")
print(coverage.isnull().sum())

print("\nSummary Statistics:")
print(coverage.describe())

print("\nNumber of Countries:", coverage["NAME"].nunique())
print("Number of Vaccines:", coverage["ANTIGEN"].nunique())
print("Year Range:", coverage["YEAR"].min(), "-", coverage["YEAR"].max())

# ------------------------------------
# Distribution of Vaccination Coverage
# ------------------------------------

OUTPUT_DIR = BASE_DIR / "outputs" / "plots"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def save_plot(filename):
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=300)
    plt.show()

# ------------------------------------
# Distribution of Vaccination Coverage
# ------------------------------------

plt.figure(figsize=(10,6))

coverage["COVERAGE"].dropna().hist(
    bins=30,
    edgecolor="black"
)

plt.title("Distribution of Vaccination Coverage")
plt.xlabel("Coverage (%)")
plt.ylabel("Frequency")

save_plot("coverage_distribution.png")

# ------------------------------------
# Top 10 Countries by Average Coverage
# ------------------------------------

print("Generating Chart 2...")

top10 = (
    coverage.groupby("NAME")["COVERAGE"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12,6))
plt.bar(top10.index, top10.values)

plt.title("Top 10 Countries by Average Vaccination Coverage")
plt.xlabel("Country")
plt.ylabel("Average Coverage (%)")
plt.xticks(rotation=45)

save_plot("top10_countries.png")
plt.close()

# ------------------------------------
# Bottom 10 Countries by Average Coverage
# ------------------------------------

bottom10 = (
    coverage.groupby("NAME")["COVERAGE"]
    .mean()
    .sort_values()
    .head(10)
)

plt.figure(figsize=(12,6))

bottom10.plot(kind="bar")

plt.title("Bottom 10 Countries by Average Vaccination Coverage")
plt.xlabel("Country")
plt.ylabel("Average Coverage (%)")
plt.xticks(rotation=45)

save_plot("bottom10_countries.png")

# ------------------------------------
# Average Coverage Over the Years
# ------------------------------------

yearly = coverage.groupby("YEAR")["COVERAGE"].mean()

plt.figure(figsize=(12,6))

yearly.plot(marker="o")

plt.title("Average Vaccination Coverage Over Time")
plt.xlabel("Year")
plt.ylabel("Average Coverage (%)")
plt.grid(True)

save_plot("coverage_trend.png")

