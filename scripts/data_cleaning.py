import pandas as pd
# Specify the file path
file_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\data\California_Fire_Perimeters_(all).csv.csv'

# Load the dataset
fire_data = pd.read_csv(file_path)
# Display the first few rows to verify the data was loaded correctly
print(fire_data.head())
# Display the dataset's structure and column information
print("Dataset Information:")
print(fire_data.info())
# Check for missing values in each column
print("\nMissing Values:")
print(fire_data.isnull().sum())
# Display basic statistics for numerical columns
print("\nDescriptive Statistics:")
print(fire_data.describe())
# Drop unnecessary columns
columns_to_drop = ['FIRE_NUM', 'COMPLEX_NAME', 'COMPLEX_ID', 'IRWINID']
fire_data_cleaned = fire_data.drop(columns=columns_to_drop)
# Display the remaining columns
print("Columns after dropping unnecessary ones:")
print(fire_data_cleaned.columns)
# Fill missing values for UNIT_ID and FIRE_NAME
fire_data_cleaned['UNIT_ID'] = fire_data_cleaned['UNIT_ID'].fillna('Unknown')
fire_data_cleaned['FIRE_NAME'] = fire_data_cleaned['FIRE_NAME'].fillna('Unknown')
# Fill missing values for COMMENTS with "No Comments"
fire_data_cleaned['COMMENTS'] = fire_data_cleaned['COMMENTS'].fillna('No Comments')
# Drop rows where INC_NUM is missing
fire_data_cleaned = fire_data_cleaned.dropna(subset=['INC_NUM'])
# Check for remaining missing values
print("Remaining Missing Values:")
print(fire_data_cleaned.isnull().sum())
# Handle missing CONT_DATE: Fill with ALARM_DATE
fire_data_cleaned['CONT_DATE'] = fire_data_cleaned['CONT_DATE'].fillna(fire_data_cleaned['ALARM_DATE'])

# Handle missing OBJECTIVE: Fill with the mode (most common value)
fire_data_cleaned['OBJECTIVE'] = fire_data_cleaned['OBJECTIVE'].fillna(fire_data_cleaned['OBJECTIVE'].mode()[0])

# Verify no missing values remain
print("Missing Values After Final Cleaning:")
print(fire_data_cleaned.isnull().sum())
# Convert ALARM_DATE and CONT_DATE to datetime format
fire_data_cleaned['ALARM_DATE'] = pd.to_datetime(fire_data_cleaned['ALARM_DATE'], errors='coerce')
fire_data_cleaned['CONT_DATE'] = pd.to_datetime(fire_data_cleaned['CONT_DATE'], errors='coerce')

# Calculate fire duration in days
fire_data_cleaned['DURATION'] = (fire_data_cleaned['CONT_DATE'] - fire_data_cleaned['ALARM_DATE']).dt.days

# Handle cases where DURATION might be negative or NaN
fire_data_cleaned['DURATION'] = fire_data_cleaned['DURATION'].fillna(0).clip(lower=0).astype(int)

# Display a summary of the DURATION column
print("Fire Duration Summary:")
print(fire_data_cleaned['DURATION'].describe())

# Preview the dataset
print("\nPreview of the Dataset with DURATION:")
print(fire_data_cleaned[['ALARM_DATE', 'CONT_DATE', 'DURATION']].head())
# Define a mapping for CAUSE values
cause_mapping = {
    1: "Human Activity",
    2: "Lightning",
    3: "Equipment Use",
    4: "Debris Burning",
    5: "Railroad",
    6: "Arson",
    7: "Vehicle",
    8: "Powerline",
    9: "Campfire",
    10: "Miscellaneous",
    11: "Structure",
    12: "Fireworks",
    13: "Smoking",
    14: "Unknown Cause",
    15: "Other Causes"
}

# Map the CAUSE column to descriptive labels
fire_data_cleaned['CAUSE'] = fire_data_cleaned['CAUSE'].map(cause_mapping).fillna('Other')

# Display the unique values in the CAUSE column
print("Unique Causes:")
print(fire_data_cleaned['CAUSE'].unique())
# Define the path for the cleaned dataset
cleaned_file_path = r'C:\Users\13176\Documents\Projects\LA_Fires_Analysis\data\cleaned_fire_data.csv'

# Save the cleaned dataset to a CSV file
fire_data_cleaned.to_csv(cleaned_file_path, index=False)

# Confirm the dataset is saved
print(f"Cleaned dataset saved to: {cleaned_file_path}")

