-- 1. Basic Dataset Overview
-- Number of countries in coverage data
SELECT 
    COUNT(DISTINCT country) AS total_countries
FROM coverage;
-- Year range available
SELECT 
    MIN(year) AS start_year,
    MAX(year) AS end_year
FROM coverage;
-- 2. Vaccination Coverage Analysis
-- Top 10 countries by average vaccination coverage
SELECT
    country,
    ROUND(AVG(coverage),2) AS average_coverage
FROM coverage
WHERE coverage IS NOT NULL
GROUP BY country
ORDER BY average_coverage DESC
LIMIT 10;
-- Bottom 10 countries by average vaccination coverage
SELECT
    country,
    ROUND(AVG(coverage),2) AS average_coverage
FROM coverage
WHERE coverage IS NOT NULL
GROUP BY country
ORDER BY average_coverage ASC
LIMIT 10;
-- Average global coverage by year
SELECT
    year,
    ROUND(AVG(coverage),2) AS average_coverage
FROM coverage
WHERE coverage IS NOT NULL
GROUP BY year
ORDER BY year;
-- 3. Disease Incidence Analysis
-- Top diseases by average incidence rate
SELECT
    disease,
    ROUND(AVG(incidence_rate),2) AS avg_incidence
FROM incidence
WHERE incidence_rate IS NOT NULL
GROUP BY disease
ORDER BY avg_incidence DESC
LIMIT 10;
-- Incidence trend by year
SELECT
    year,
    ROUND(AVG(incidence_rate),2) AS avg_incidence
FROM incidence
WHERE incidence_rate IS NOT NULL
GROUP BY year
ORDER BY year;
-- 4. Reported Cases Analysis
-- Diseases with highest reported cases
SELECT
    disease,
    SUM(cases) AS total_cases
FROM reported_cases
WHERE cases IS NOT NULL
GROUP BY disease
ORDER BY total_cases DESC
LIMIT 10;
-- Countries with highest reported cases
SELECT
    country,
    SUM(cases) AS total_cases
FROM reported_cases
WHERE cases IS NOT NULL
GROUP BY country
ORDER BY total_cases DESC
LIMIT 10;
-- 5. Vaccine Introduction Analysis
-- Number of vaccines introduced each year
SELECT
    year,
    COUNT(*) AS vaccines_introduced
FROM vaccine_introduction
WHERE intro = 'Yes'
GROUP BY year
ORDER BY year;
-- Countries introducing the most vaccines
SELECT
    countryname,
    COUNT(*) AS total_vaccines
FROM vaccine_introduction
WHERE intro = 'Yes'
GROUP BY country
ORDER BY total_vaccines DESC
LIMIT 10;
-- 6. Vaccine Schedule Analysis
-- Most commonly scheduled vaccines
SELECT
    vaccine_description,
    COUNT(*) AS schedule_count
FROM vaccine_schedule
GROUP BY vaccine_description
ORDER BY schedule_count DESC
LIMIT 10;
-- Vaccine schedule by region
SELECT
    who_region,
    COUNT(*) AS total_schedules
FROM vaccine_schedule
GROUP BY who_region
ORDER BY total_schedules DESC;
-- 7. Advanced Query (JOIN)
-- Compare vaccination coverage with disease cases
SELECT
    c.country,
    ROUND(AVG(c.coverage),2) AS avg_coverage,
    SUM(r.cases) AS total_cases
FROM coverage c
JOIN reported_cases r
ON c.country = r.country
GROUP BY c.country
ORDER BY total_cases DESC
LIMIT 10;