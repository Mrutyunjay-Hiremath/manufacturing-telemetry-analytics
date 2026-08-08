import json
import pandas as pd

# Load the JSON data
# Note: Update 'daikibo_data.json' to the exact name of your downloaded file
file_path = 'C:/Users/anime/Projects/manufacturing-telemetry-analytics/data/raw/daikibo_data.json' 
df = pd.read_json(file_path)

print(f"Dataset contains {df.shape[0]} rows and {df.shape[1]} columns.\n")

# Peek at the first 5 rows
df.head()

# Check data types (look out for date columns acting as strings)
print("--- Data Types & Non-Null Counts ---")
df.info()

print("\n--- Missing Values Check ---")
print(df.isnull().sum())

# Assuming standard column names for IoT data (adjust if your dataset differs)
print("--- Factory Locations ---")
print(df['location'].value_counts()) 

print("\n--- Machine Types ---")
print(df['device'].value_counts()) 

print("\n--- Status Breakdown ---")
print(df['status'].value_counts())
