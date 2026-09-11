# Logistics Data Cleaning & Preprocessing

**Yuva Intern Logistics Data Analyst Internship – Week 2 Task**

This project demonstrates a practical logistics data collection, cleaning, and preprocessing workflow using Python and pandas.

## Project Objective

Prepare a logistics shipment dataset for reliable downstream analysis by identifying and correcting common data-quality problems while keeping the preprocessing workflow reproducible.

## Data Quality Issues Covered

- Missing numerical values
- Missing categorical values
- Duplicate shipment records
- Inconsistent categorical formatting
- Mixed date formats
- Numeric values containing text such as `550 km`
- Outliers in operational variables
- Data-type inconsistencies

## Preprocessing Workflow

1. Load the raw CSV with pandas.
2. Inspect shape, data types, missing values, and duplicates.
3. Standardize column names and categorical text.
4. Convert shipment and delivery dates to datetime.
5. Convert numeric fields safely.
6. Remove duplicate shipment IDs.
7. Impute missing numerical values using the median.
8. Fill missing categorical values with `Unknown`.
9. Create shipment duration as a derived feature.
10. Treat outliers using the IQR method.
11. Validate the cleaned dataset.
12. Export the cleaned dataset.

## Repository Structure

```text
logistics-data-cleaning-preprocessing/
├── data/
│   └── logistics_data.csv
├── src/
│   └── analysis.py
├── requirements.txt
└── README.md
```

## How to Run

```bash
git clone https://github.com/ankitsharma-data/logistics-data-cleaning-preprocessing.git
cd logistics-data-cleaning-preprocessing
pip install -r requirements.txt
python src/analysis.py
```

The script creates `data/logistics_data_cleaned.csv` after preprocessing.

## Tools

- Python
- pandas
- NumPy-compatible data processing concepts

## Author

**Ankit Sharma**  
BCA Student | Aspiring Data Analyst
