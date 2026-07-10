# Global Vaccination Coverage Analysis Dashboard

## Project Overview

The **Global Vaccination Coverage Analysis Dashboard** is an end-to-end data analytics project that analyzes worldwide vaccination coverage, vaccine distribution trends, and country-level healthcare insights.

The project combines **Python, SQL, and Power BI** to clean, transform, analyze, and visualize vaccination datasets to identify global patterns and trends.

The final interactive dashboard provides insights into vaccination coverage across countries, years, and vaccine categories.

---

# Objectives

- Analyze global vaccination coverage trends over time
- Identify countries with the highest vaccination coverage
- Compare vaccination performance across different vaccines
- Understand global distribution patterns
- Create an interactive business intelligence dashboard using Power BI

---

# Tech Stack

### Programming & Data Processing
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Database
- SQL
- Data modeling
- Analytical queries

### Visualization
- Microsoft Power BI
- Interactive dashboards
- Data storytelling

### Development Tools
- Git & GitHub
- VS Code

---

# Project Structure

```
Global-Vaccination-Coverage-Analysis/

│
├── data/
│   └── Raw vaccination datasets
│
├── script/
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── create_sample.py
│   └── fix_schedule_csv.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── outputs/
│   ├── plots/
│   └── sql_results/
│
├── powerbi/
│   └── Global_Vaccination_Coverage_Dashboard.pbix
│
├── screenshots/
│   └── vaccination_dashboard.png
│
├── requirements.txt
└── README.md
```

---

# Dashboard Features

The Power BI dashboard includes:

### Key Performance Indicators

- Total Countries Analyzed: **242**
- Total Vaccination Records: **50K+**
- Total Vaccine Doses: **34.02 Billion**
- Average Vaccination Coverage: **77.87%**

---

# Visualizations Included

### 1. Vaccination Coverage Trend Over Years

Shows how global vaccination coverage has changed over time.

### 2. Top 10 Countries by Vaccination Coverage

Identifies countries achieving the highest vaccination coverage rates.

### 3. Average Coverage by Antigen

Compares coverage levels across different vaccines.

### 4. Global Vaccination Coverage Map

Displays country-wise vaccination distribution.

### 5. KPI Summary Cards

Provides a quick overview of major vaccination statistics.

---

# Data Analysis Performed

## Data Cleaning

Performed:

- Missing value handling
- Data type corrections
- Dataset restructuring
- Data preparation for analysis

## Exploratory Data Analysis

Analyzed:

- Coverage trends
- Country-level performance
- Vaccine-wise distribution
- Global vaccination patterns

## SQL Analysis

Created queries to answer:

- Which countries have the highest vaccination coverage?
- What are the most common vaccines?
- How has vaccination changed over time?
- Which diseases have the highest reported cases?

---

# Dashboard Preview

![Power BI Dashboard](screenshots/vaccination_dashboard.png)

---

# How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/PragatiMaurya16/Global-Vaccination-Coverage-Analysis.git
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Analysis Scripts

Example:

```bash
python script/data_cleaning.py

python script/eda.py
```

### 5. Open Dashboard

Open:

```
powerbi/Global_Vaccination_Coverage_Dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# Key Insights

- Global vaccination coverage has improved significantly over the years.
- Several countries achieved vaccination coverage above 90%.
- Vaccine performance varies across different antigens.
- Healthcare access and vaccination programs influence country-level differences.

---

# Future Improvements

- Add interactive Streamlit web application
- Integrate real-time vaccination APIs
- Add predictive models for future coverage trends
- Deploy dashboard online

---

# Author

**Pragati Maurya**

GitHub:
https://github.com/PragatiMaurya16

---
