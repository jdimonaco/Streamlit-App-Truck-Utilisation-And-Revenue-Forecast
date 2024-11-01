import pandas as pd
from data_cleaner import DataCleaner
from fleet_analysis import FleetAnalysis


# Read the data from CSV
def main():
    data = pd.read_csv("truck_utilisation.csv")
    # Convert the 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')  

    # Calling the methods 
    data_cleaner = DataCleaner(data)  # Create an instance of DataCleaner class
    df_cleaned = data_cleaner.handle_missing_values()  # Clean the dataset by handling missing values
    df_cleaned = data_cleaner.remove_duplicates()  # Remove duplicate rows from the dataset

    fleet_analysis = FleetAnalysis(df_cleaned)  # Create an instance of FleetAnalysis class on the cleaned data 
    df_cleaned = fleet_analysis.calculate_utilisation()  # Calculate utilisation and add it as a new column
    model, mae, df_cleaned = fleet_analysis.predict_revenue()  # Train a model to predict revenue and calculate the mean absolute error

    print("Model trained and evaluated successfully.")
    print(df_cleaned.head())

if __name__ == "__main__":
    main()