import pandas as pd
from data_cleaner import DataCleaner
from fleet_analysis import FleetAnalysis


# Main function to execute data processing and analysis 
def main():
    # Load data from a CSV file
    data = pd.read_csv("truck_utilisation.csv")

    # Convert the 'Date' column to datetime format
    data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')  

    # Initialise the DataCleaner with the raw data for preprocessing
    data_cleaner = DataCleaner(data)  # Create an instance of DataCleaner class 
    df_cleaned = data_cleaner.handle_missing_values()  # Clean the dataset by handling missing values
    df_cleaned = data_cleaner.remove_duplicates()  # Remove duplicate rows from the dataset

    # Initialise the FleetAnalysis with the cleaned data for analysis
    fleet_analysis = FleetAnalysis(df_cleaned)  # Create an instance of FleetAnalysis class 
    df_cleaned = fleet_analysis.calculate_utilisation()  # Calculate utilisation and add it as a new column
    model, mae, df_cleaned = fleet_analysis.predict_revenue()  # Train a model to predict revenue and calculate the mean absolute error

    print("Model trained and evaluated successfully.")
    print(df_cleaned.head())

#Execute the main function only if the script is run directly
if __name__ == "__main__":
    main()