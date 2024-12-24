import pandas as pd

#Define a class for preprocessing steps
class DataCleaner:
    def __init__(self,data) -> None:
        """Initialise the DataCleaner class."""
        self.data = data

    def handle_missing_values(self) -> pd.DataFrame:
        """Drop rows with missing shipment_id."""
        self.data = self.data.dropna(subset=['shipment_id'])

        #Function to fill missing values in columns with their respective mean values.
        def fill_with_mean(column_name) -> None:
            self.data[column_name] = self.data[column_name].fillna(self.data[column_name].mean())

        #Define a variable with the list of columns to fill missing values.
        columns_with_missing_values = ['weight','cbm','daily_cost', 'total_revenue']

        #Loop through each column in the list (columns_with_missing_values) and use the fill_with_mean function to handle missing values.
        for column in columns_with_missing_values:
            fill_with_mean(column)
        
        return self.data
    
    def remove_duplicates(self) -> pd.DataFrame:
        """Remove duplicate rows based on shipment_id."""
        self.data = self.data.drop_duplicates(subset=['shipment_id']) 
        return self.data
