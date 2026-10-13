import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score


# Road freight convention: 1 cubic metre (cbm) of cargo is charged as 333 kg.
# Used to turn volume into a volumetric weight so it can be compared with weight and capacity (kg).
VOLUMETRIC_FACTOR = 333


# Define a class for the fleet analysis with methods to calculate utilisation and predict revenues.
class FleetAnalysis:
    def __init__(self, data) -> None:
        """Initialise the FleetAnalysis class."""
        self.data = data
    
    # Calculate freight over or under utilisation
    def calculate_utilisation(self) -> pd.DataFrame:
        def utilisation(row) -> str:
            """Calculates the chargeable weight: the larger of actual weight and volumetric weight (cbm x 333 kg)."""
            volumetric_weight = row['cbm'] * VOLUMETRIC_FACTOR
            chargeable_weight = max(row['weight'], volumetric_weight)
            """If chargeable weight is greater than capacity return overutilisation else underutilisation."""
            if chargeable_weight > row['capacity']:
                return "Overutilisation" # Return "Overutilisation" if the limit is exceeded
            else:
                return "Underutilisation" # Return "Underutilisation" otherwise
        
        # Apply this function to each row and add the result as a new column called utilisation
        self.data['Utilisation'] = self.data.apply(utilisation, axis=1)
        print("Data after adding Utilisation column:")
        return self.data

    # Predict revenue
    def predict_revenue(self) -> tuple:
        # Drop columns before splitting the dataset
        data_dropped = self.data.drop(columns=['shipment_id', 'Date', 'truck_type', 'Utilisation'])
        
        # Select features (X) and the target variable (y)
        X = data_dropped.drop(columns=['total_revenue'])  # Exclude 'total_revenue' column from features
        y = data_dropped['total_revenue']   # Select the target column I want to predict 
        
        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        
        # Predict and calculate mean absolute error
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        print(f"Mean Absolute Error: {mae}")

        # Add predicted revenue and revenue difference to the data
        self.data['predicted_revenue'] = model.predict(X)
        self.data['revenue_difference'] = self.data['total_revenue'] - self.data['predicted_revenue']
        
        return model, mae, self.data
