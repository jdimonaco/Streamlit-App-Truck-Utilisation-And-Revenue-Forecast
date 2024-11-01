import pandas as pd

#Define a class for preprocessing steps
class DataCleaner:
    def __init__(self,data) -> None:
        self.data = data

    def handle_missing_values(self):
        """Drop rows with missing shipment_id."""
        self.data = self.data.dropna(subset=['shipment_id'])
        """Fills missing values in weight, cbm, daily_cost, and total_revenue columns with their respective mean values."""
        self.data['weight'] = self.data['weight'].fillna(self.data['weight'].mean())
        self.data['cbm'] = self.data['cbm'].fillna(self.data['cbm'].mean())
        self.data['daily_cost'] = self.data['daily_cost'].fillna(self.data['daily_cost'].mean())
        self.data['total_revenue'] = self.data['total_revenue'].fillna(self.data['total_revenue'].mean())
        return self.data
    
    def remove_duplicates(self):
        """Remove duplicate rows based on shipment_id."""
        self.data = self.data.drop_duplicates(subset=['shipment_id'])
        return self.data
