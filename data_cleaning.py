
import pandas as pd
import numpy as np

# Load the raw dataset
df = pd.read_csv("task1_raw_dataset.csv")

# Display the first five records
print("FIRST FIVE RECORDS:")
print(df.head())

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Check missing values
print("\nMISSING VALUES:")
print(df.isnull().sum())

# Check duplicate records
print("\nDUPLICATE RECORDS:")
print(df.duplicated().sum())

# STEP 2: DUPLICATE DETECTION

print("\nDUPLICATE RECORDS:")
print(df[df.duplicated()])

print("\nTOTAL DUPLICATES:")
print(df.duplicated().sum())

# Remove duplicate records
df.drop_duplicates(inplace=True)

print("\nDATASET AFTER DUPLICATE REMOVAL:")
print("Total rows:", len(df))
print("Remaining duplicates:", df.duplicated().sum())

# STEP 3: MISSING VALUE HANDLING

print("\nMISSING VALUES BEFORE CLEANING:")
print(df.isnull().sum())

# Replace invalid salary text with missing values
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

# Replace missing email values
df["Email"] = df["Email"].fillna("Not Provided")

# Calculate median salary
median_salary = df["Salary"].median()

# Replace missing salary with median
df["Salary"] = df["Salary"].fillna(median_salary)

print("\nMISSING VALUES AFTER CLEANING:")
print(df.isnull().sum())

print("\nMEDIAN SALARY USED:")
print(median_salary)

# STEP 4: DATA STANDARDIZATION

# Standardize city names
df["City"] = df["City"].str.strip().str.title()

# Standardize employment status
df["Status"] = df["Status"].str.strip().str.title()

# Standardize email addresses
df["Email"] = df["Email"].str.strip().str.lower()


# Convert dates using their original formats

def clean_date(date):
    date = str(date).strip()

    formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%b %d %Y",
        "%d-%m-%Y"
    ]

    for fmt in formats:
        try:
            return pd.to_datetime(date, format=fmt)
        except ValueError:
            continue

    return pd.NaT


df["Joining_Date"] = df["Joining_Date"].apply(clean_date)

print("\nCORRECTED JOINING DATES:")
print(df[["Employee_ID", "Joining_Date"]].head(10))



# Display standardized data
print("\nDATA AFTER STANDARDIZATION:")
print(df[["City", "Status", "Joining_Date"]].head(10))

print("\nSTANDARDIZED CITY VALUES:")
print(df["City"].unique())

print("\nSTANDARDIZED STATUS VALUES:")
print(df["Status"].unique())

print("\nDATE DATA TYPE:")
print(df["Joining_Date"].dtype)

# STEP 5: STRUCTURAL VALIDATION

print("\n========== STRUCTURAL VALIDATION ==========")

# Check unique Employee IDs
print("Unique Employee IDs:",
      df["Employee_ID"].is_unique)

# Check missing Employee IDs
print("Missing Employee IDs:",
      df["Employee_ID"].isnull().sum())

# Check salary data type
print("Salary is numeric:",
      pd.api.types.is_numeric_dtype(df["Salary"]))

# Check positive salaries
print("All salaries are positive:",
      (df["Salary"] > 0).all())

# Check valid dates
print("All joining dates are valid:",
      df["Joining_Date"].notnull().all())

# Check allowed employment statuses
print("Valid employment statuses:",
      df["Status"].isin(["Active", "Inactive"]).all())

# Check duplicate records
print("No duplicate records:",
      not df.duplicated().any())

# Check all missing values
print("No missing values:",
      not df.isnull().any().any())


# STEP 6: EXPORT CLEANED DATASET

export_df = df.copy()

# Save dates in YYYY-MM-DD format
export_df["Joining_Date"] = (
    export_df["Joining_Date"].dt.strftime("%Y-%m-%d")
)

export_df.to_csv("cleaned_dataset.csv", index=False)

print("\nCleaned dataset exported successfully!")

print("Final dataset shape:", export_df.shape)
