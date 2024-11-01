import pandas as pd
from data_cleaner import DataCleaner
from fleet_analysis import FleetAnalysis


# Read the data from CSV
data = pd.read_csv("truck_utilisation.csv")
print(data.head())

# Initialise the DataCleaner class with initial data
data_cleaner = DataCleaner(data)


# Test handle_missing_values Method
print(f"\nBefore handling missing values:\n{data.isnull().sum()}")  # Check for missing values on initial data
df_cleaned = data_cleaner.handle_missing_values()
print(f"\nAfter handling missing values:\n{df_cleaned.isnull().sum()}")  # Check for any remaining missing values on cleaned data

# Test remove_duplicates Method
print(f"\nBefore removing duplicates:\n{data.duplicated(subset=['shipment_id']).sum()}")  # Check for duplicates on initial data
df_cleaned = data_cleaner.remove_duplicates()
print(f"\nAfter removing duplicates:\n{df_cleaned.duplicated(subset=['shipment_id']).sum()}")  # Check if duplicates are removed on cleaned data


# Initialise the FleetAnalysis class with the cleaned data
fleet_analysis = FleetAnalysis(df_cleaned)

# Test calculate_utilisation Method
print(f"\nBefore calculating utilisation:\n{df_cleaned[['weight', 'cbm', 'capacity']].head()}") # Check the first few rows before adding Utilisation
df_cleaned = fleet_analysis.calculate_utilisation()
print(f"\nAfter calculating utilisation:\n{df_cleaned[['weight', 'cbm', 'capacity', 'Utilisation']].head()}")   # Check the first few rows after adding Utilisation

# Test predict_revenue Method
model, mae, df_cleaned = fleet_analysis.predict_revenue()
print(f"\nMean Absolute Error: {mae}")  # Print the MAE to evaluate model performance

# Print the data with predicted revenue and difference
print(f"\nData with Predicted Revenue and Difference:\n{df_cleaned[['total_revenue', 'predicted_revenue', 'revenue_difference']].head()}")