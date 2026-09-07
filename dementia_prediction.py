import pandas as pd

# Load dataset
df = pd.read_csv("data/dementia_patients_health_data.csv")

# Dataset shape
print("Dataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Dataset information
print("\nDataset Information:")
df.info()

# Target distribution
print("\nDementia Distribution:")
print(df["Dementia"].value_counts())
