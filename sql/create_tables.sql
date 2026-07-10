USE vaccination_analysis;

-- =========================================
-- Coverage Table
-- =========================================

CREATE TABLE coverage (

id INT AUTO_INCREMENT PRIMARY KEY,

group_name VARCHAR(50),

code VARCHAR(10),

country VARCHAR(150),

year INT,

antigen VARCHAR(50),

antigen_description VARCHAR(255),

coverage_category VARCHAR(100),

coverage_category_description VARCHAR(255),

target_number DOUBLE,

doses DOUBLE,

coverage DOUBLE

);

-- =========================================
-- Incidence Table
-- =========================================

CREATE TABLE incidence (

id INT AUTO_INCREMENT PRIMARY KEY,

group_name VARCHAR(50),

code VARCHAR(10),

country VARCHAR(150),

year INT,

disease VARCHAR(150),

disease_description VARCHAR(255),

denominator VARCHAR(255),

incidence_rate DOUBLE

);

-- =========================================
-- Reported Cases Table
-- =========================================

CREATE TABLE reported_cases (

id INT AUTO_INCREMENT PRIMARY KEY,

group_name VARCHAR(50),

code VARCHAR(10),

country VARCHAR(150),

year INT,

disease VARCHAR(150),

disease_description VARCHAR(255),

cases DOUBLE

);

-- =========================================
-- Vaccine Introduction Table
-- =========================================

CREATE TABLE vaccine_introduction (

id INT AUTO_INCREMENT PRIMARY KEY,

iso_code VARCHAR(10),

country VARCHAR(150),

who_region VARCHAR(50),

year INT,

description VARCHAR(255),

intro VARCHAR(20)

);

-- =========================================
-- Vaccine Schedule Table
-- =========================================

CREATE TABLE vaccine_schedule (

id INT AUTO_INCREMENT PRIMARY KEY,

iso_code VARCHAR(10),

country VARCHAR(150),

who_region VARCHAR(50),

year INT,

vaccine_code VARCHAR(50),

vaccine_description VARCHAR(255),

schedule_rounds DOUBLE,

target_population VARCHAR(255),

target_population_description VARCHAR(255),

geo_area VARCHAR(100),

age_administered VARCHAR(100),

source_comment TEXT

);