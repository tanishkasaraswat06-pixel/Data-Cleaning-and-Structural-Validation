# Data Cleaning & Structural Validation

## Project Overview
This project focuses on transforming raw, unstructured employee data into a clean, consistent, and reliable format using Python.

The dataset contains duplicate records, missing values, inconsistent formats, and invalid entries. The objective is to clean the data while maintaining its integrity and ensuring structural accuracy.

## Objectives
- Identify and remove duplicate records.
- Handle missing and invalid values.
- Standardize city names and employment statuses.
- Convert inconsistent date formats into a standard format.
- Validate employee IDs, salaries, dates, and data types.
- Export the final cleaned dataset.

## Tools & Technologies
- Python
- Pandas
- NumPy
- Visual Studio Code

## Project Files
- `task1_raw_dataset.csv` – Original raw dataset.
- `data_cleaning.py` – Python script for data cleaning and validation.
- `cleaned_dataset.csv` – Final cleaned dataset.
- `requirements.txt` – Required Python libraries.

## Data Cleaning Operations
1. Duplicate detection and removal.
2. Missing value treatment.
3. Salary conversion and median imputation.
4. City and status standardization.
5. Date format correction.
6. Structural validation.

## Validation Results
- Unique Employee IDs: Passed
- Missing Employee IDs: 0
- Numeric Salary Validation: Passed
- Positive Salary Validation: Passed
- Valid Joining Dates: Passed
- Valid Employment Statuses: Passed
- Duplicate Records: 0
- Missing Values: 0

## Final Dataset
- Original Records: 25
- Duplicate Records Removed: 1
- Final Records: 24
- Total Columns: 7

## How to Run the Project

1. Clone or download this repository.
2. Install dependencies:

   `pip install -r requirements.txt`

3. Run the Python script:

   `python data_cleaning.py`

4. The cleaned dataset will be generated as `cleaned_dataset.csv`.

## Conclusion
The project successfully transforms an inconsistent raw dataset into a structured and validated dataset. It demonstrates practical data cleaning, preprocessing, and validation techniques using Python.

**Note:** The employee dataset used in this project is synthetic and created for educational purposes.