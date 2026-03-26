# New Zealand Economic Dashboard: Unemployment & Economic Indicators Analysis

<img width="663" height="411" alt="image" src="https://github.com/user-attachments/assets/96ce632e-dc0d-415b-a2af-1cdad24295c6" />

<img width="884" height="341" alt="image" src="https://github.com/user-attachments/assets/d5920ea6-b654-4006-a4b5-7de11c15e89d" />

<img width="771" height="367" alt="image" src="https://github.com/user-attachments/assets/245a4299-9391-4fa4-b63b-ec651a789fc1" />


An interactive Power BI dashboard analyzing the relationship between unemployment rates and key economic indicators in New Zealand, featuring predictive forecasting and regional comparisons.

## 📊 Project Overview

This project explores the economic landscape of New Zealand through data-driven visualization and analysis. By combining multiple authoritative data sources, I've created an interactive dashboard that tracks unemployment trends alongside critical economic indicators like inflation, GDP, and interest rates over a 20+ year period.

### Key Features
- **Time Series Analysis**: 20+ years of quarterly economic data with built-in forecasting
- **Economic Correlation Analysis**: Interactive scatter plots showing relationships between unemployment and key economic drivers
- **Regional Comparisons**: Geographical breakdown comparing unemployment across NZ regions
- **Predictive Insights**: 4-8 quarter unemployment forecasting using Power BI's built-in analytics
- **Interactive Dashboard**: Fully interactive with slicers for date ranges and region selection

## 🗂️ Data Sources

| Source | Data | Time Period |
|--------|------|-------------|
| Stats NZ (Infoshare) | Quarterly unemployment rates with regional breakdowns | 2000-2024 |
| Reserve Bank of New Zealand (RBNZ) | Official cash rate, CPI inflation data | 2000-2024 |
| World Bank | New Zealand GDP growth rates | 2000-2024 |

## 🛠️ Technology Stack

- **Data Processing**: Python (Pandas) for data cleaning and transformation
- **Visualization**: Microsoft Power BI
- **Data Analysis**: DAX (Data Analysis Expressions)
- **Forecasting**: Power BI built-in forecasting engine

## 📁 Project Structure

## 🔄 Data Processing Workflow

### 1. Data Collection
Data was downloaded from official NZ government sources (Stats NZ, RBNZ) and the World Bank covering 2000-2024.

### 2. Data Cleaning (Python)

#### Key cleaning steps performed:
- Standardized date formats to YYYY-QQ format
- Harmonized regional naming conventions across datasets
- Handled missing values using forward-fill methodology
- Merged all datasets into a single master table
- Validated data consistency and outlier detection

### 3. Power BI Data Model

- Created a comprehensive date table for time intelligence
- Established relationships between the master fact table and dimension tables
- Implemented row-level security considerations for regional data

### 4. DAX Measures Created

### 5. Dashboard Pages
