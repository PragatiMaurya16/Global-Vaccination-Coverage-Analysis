# Global Vaccination Coverage Analysis Dashboard

## Dashboard Preview

![Power BI Dashboard](screenshots/vaccination_dashboard.png)

## Project Overview

The **Global Vaccination Coverage Analysis Dashboard** is an end-to-end data analytics project that analyzes worldwide vaccination coverage, vaccine distribution trends, and country-level healthcare insights.

This project combines **Python, SQL, and Power BI** to clean, transform, analyze, and visualize vaccination datasets.

The objective is to understand vaccination patterns across countries, identify coverage trends over time, compare vaccine performance, and present meaningful insights through an interactive Power BI dashboard.

---

# Project Highlights

- End-to-end data analytics workflow
- Data cleaning and preprocessing using Python
- Exploratory Data Analysis (EDA)
- SQL-based data analysis
- Interactive Power BI dashboard development
- Analysis of **50K+ vaccination records**
- Coverage analysis across **242 countries**
- Data visualization and storytelling

---

# Project Objectives

The main goals of this project are:

- Analyze global vaccination coverage trends over time
- Identify countries with the highest vaccination coverage
- Compare vaccination performance across different vaccines
- Understand vaccine distribution patterns
- Create an interactive business intelligence dashboard
- Extract meaningful healthcare insights from vaccination data

---

# Dataset Description

The dataset contains global vaccination-related information including:

- Country
- Year
- Vaccine antigen
- Vaccination coverage percentage
- Number of doses
- Vaccine introduction information
- Disease incidence data
- Reported cases

The raw dataset was cleaned and transformed before performing analysis.

---

# Tech Stack

## Programming & Data Processing

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Database & Querying

- MySQL
- SQL Queries
- Data Modeling

## Visualization

- Microsoft Power BI
- Interactive Dashboards
- Data Storytelling

## Development Tools

- Git
- GitHub
- VS Code

---

# Project Structure

```
Global-Vaccination-Coverage-Analysis/

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
├── script/
│   ├── create_sample.py
│   ├── data_cleaning.py
│   ├── eda.py
│   └── fix_schedule_csv.py
│
├── sql/
│   ├── create_database.sql
│   ├── create_tables.sql
│   └── analysis_queries.sql
│
├── requirements.txt
└── README.md
```

---

# Project Workflow

```
Raw Dataset
      ↓
Data Cleaning using Python
      ↓
Exploratory Data Analysis
      ↓
Data Storage & Analysis using MySQL
      ↓
SQL Queries & Insights
      ↓
Power BI Dashboard
      ↓
Data Visualization & Reporting
```

---

# Data Cleaning & Preparation

Performed data preprocessing steps including:

- Handling missing values
- Correcting data types
- Removing inconsistencies
- Preparing structured datasets
- Creating analysis-ready tables

---

# Exploratory Data Analysis

Performed analysis to understand:

- Vaccination coverage trends
- Country-wise vaccination performance
- Vaccine distribution patterns
- Disease incidence trends
- Global vaccination changes over time

---

# SQL Analysis

Created SQL queries to analyze:

- Top countries by vaccination coverage
- Vaccination trends over years
- Commonly used vaccines
- Vaccine introduction patterns
- Disease incidence patterns
- Country-level comparisons

---

# Power BI Dashboard

The interactive Power BI dashboard includes:

## KPI Cards

- Total Countries Analyzed: **242**
- Total Vaccination Records: **50K+**
- Average Vaccination Coverage: **77.87%**
- Total Vaccine Doses: **34.02 Billion**

---

## Visualizations Included

### 1. Vaccination Coverage Trend Over Years

Shows how vaccination coverage has changed globally over time.

---

### 2. Top 10 Countries by Vaccination Coverage

Highlights countries achieving the highest vaccination coverage rates.

---

### 3. Average Coverage by Antigen

Compares vaccination coverage across different vaccine categories.

---

### 4. Global Vaccination Coverage Map

Provides geographical analysis of vaccination coverage across countries.

> Note: Azure Maps availability depends on Power BI tenant settings and regional restrictions.

---

# Key Insights

- Global vaccination coverage has improved significantly over time.
- Average vaccination coverage across analyzed records is approximately **78%**.
- Several countries achieved vaccination coverage above **90%**.
- Vaccination performance varies across different vaccine antigens.
- Healthcare programs and accessibility influence country-level vaccination differences.

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/PragatiMaurya16/Global-Vaccination-Coverage-Analysis.git
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run Python Scripts

Example:

```bash
python script/data_cleaning.py

python script/eda.py
```

---

## 5. Run SQL Analysis

Execute SQL files inside:

```
sql/
```

using MySQL.

---

## 6. Open Power BI Dashboard

Open:

```
powerbi/Global_Vaccination_Coverage_Dashboard.pbix
```

using Microsoft Power BI Desktop.

---

# Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis
- Python Programming
- SQL Query Writing
- Database Management
- Data Visualization
- Power BI Dashboard Development
- Business Intelligence
- Data Storytelling

---

# Future Improvements

Possible improvements:

- Build a Streamlit web application
- Integrate real-time vaccination APIs
- Add predictive models for future vaccination trends
- Deploy dashboard online
- Automate data updates

---

# Author

**Pragati Maurya**

B.Tech Student | Machine Learning & Data Science Enthusiast | Aspiring Python Developer & Data Scientist

Passionate about building data-driven solutions using Python, SQL, Machine Learning, and Data Visualization.

Interested in solving real-world problems through analytics and intelligent systems.

---



If you found this project useful, consider giving it a star!
