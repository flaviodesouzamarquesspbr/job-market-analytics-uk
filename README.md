# Job Market Analytics (UK)

## 📊 Overview

This project is an end-to-end data pipeline that analyzes job market trends in the UK using real job data from the Adzuna API.

The pipeline extracts, transforms, and loads data into a structured format for business intelligence analysis, culminating in an interactive dashboard built with Tableau.

The goal is to simulate a real-world data analytics workflow, combining data engineering and data analysis practices.

## 🏗️ Architecture

The project follows a layered data architecture:

- **Bronze Layer**: Raw data ingestion from API
- **Silver Layer**: Data cleaning and transformation
- **Gold Layer**: Aggregated and analysis-ready dataset

## 🔄 Data Pipeline

1. Extract data from Adzuna API (Python)
2. Store raw data (Parquet)
3. Transform and clean data (Pandas)
4. Generate analytics dataset (CSV)
5. Visualize insights (Tableau)


## 🛠️ Tech Stack

- Python (Pandas, Requests)
- Parquet / CSV
- Tableau Public
- Git & GitHub

## 📊 Dashboard

👉 [View Dashboard](https://public.tableau.com/app/profile/flavio.marques3883/viz/job-market-insights-uk/Dashboard1)

## 📈 Key Insights

- Engineering roles tend to have the highest average salaries
- Contract types vary significantly across job categories
- Some categories have limited salary transparency

## 🚀 Future Improvements

- Add support for multiple countries
- Implement CI/CD pipeline
- Improve salary normalization and currency conversion
- Add time-series analysis

## 🧠 Learnings

- Built an end-to-end data pipeline
- Worked with real-world API data
- Applied data cleaning and transformation techniques
- Developed interactive dashboards for business insights