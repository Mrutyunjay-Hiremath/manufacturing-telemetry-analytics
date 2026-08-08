import json
import pandas as pd

def clean_telemetry_data():
    print("--- Starting Data Preparation ---\n")
    
    # 1. Load the raw JSON
    file_path = 'C:/Users/anime/Projects/manufacturing-telemetry-analytics/data/raw/daikibo_data.json'
    print(f"Loading raw data from {file_path}...")
    df = pd.read_json(file_path)
    
    # 2. Flatten the 'location' dictionary
    print("Flattening the 'location' column...")
    # This turns the dictionary keys (country, city, factory) into their own columns
    location_expanded = df['location'].apply(pd.Series)
    
    # 3. Flatten the 'data' dictionary (where our status lives!)
    print("Flattening the 'data' column...")
    data_expanded = df['data'].apply(pd.Series)
    
    # 4. Combine everything together
    print("Combining into a single flat dataset...")
    # Drop the original nested columns and attach our new clean columns
    df_clean = pd.concat([df.drop(['location', 'data'], axis=1), location_expanded, data_expanded], axis=1)
    
    # Let's peek at the new columns to make sure it worked
    print("\nNew columns available:")
    print(df_clean.columns.tolist())
    
    # 5. Export to CSV
    output_path = 'C:/Users/anime/Projects/manufacturing-telemetry-analytics/data/processed/daikibo_telemetry_clean.csv'
    print(f"\nExporting clean data to {output_path}...")
    df_clean.to_csv(output_path, index=False)
    
    print("Done! You are ready for Tableau.")

if __name__ == "__main__":
    clean_telemetry_data()