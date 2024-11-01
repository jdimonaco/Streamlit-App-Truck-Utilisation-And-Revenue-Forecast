import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from data_cleaner import DataCleaner
from fleet_analysis import FleetAnalysis

st.title("Fleet Utilisation and Revenue Prediction")

# Initialise session state variables to store data and states
if 'fleet_analysis' not in st.session_state:
    st.session_state.fleet_analysis = None
if 'predicted' not in st.session_state:
    st.session_state.predicted = False
if 'df_cleaned' not in st.session_state:
    st.session_state.df_cleaned = None

# Widget to upload CSV file
uploaded_file = st.file_uploader("Upload Truck Utilisation Data (CSV)", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Original Data", df)

    # Initialise the DataCleaner class 
    data_cleaner = DataCleaner(df)

    # Button to clean the data
    if st.button("Clean Data"):
        # Handle missing values and display the count of remaining missing values
        df_cleaned = data_cleaner.handle_missing_values()
        st.write("Missing Values After Cleaning", df_cleaned.isnull().sum())

        # Remove duplicates and display the count of remaining duplicates
        df_cleaned = data_cleaner.remove_duplicates()
        st.write("Duplicates After Cleaning", df_cleaned.duplicated(subset=['shipment_id']).sum())

        # Store cleaned data in session state
        st.session_state.df_cleaned = df_cleaned

        # Initialise FleetAnalysis with cleaned data
        st.session_state.fleet_analysis = FleetAnalysis(st.session_state.df_cleaned)

        # Calculate utilisation and update session state
        st.session_state.df_cleaned = st.session_state.fleet_analysis.calculate_utilisation()
        st.write("Utilisation Column", st.session_state.df_cleaned[['weight', 'cbm', 'capacity', 'Utilisation']].head()) 
        st.write("Cleaned Data", st.session_state.df_cleaned) 

# Predict revenue if fleet_analysis is initialised and df_cleaned is available
if st.session_state.fleet_analysis:
    if st.button("Predict Revenue"):
        model, mae, st.session_state.df_cleaned = st.session_state.fleet_analysis.predict_revenue()
        st.write(f"Model Mean Absolute Error: {mae}")
        st.session_state.predicted = True

# Show graph if prediction has been made
if st.session_state.predicted:
    if st.button("Show Graph"):
        if 'predicted_revenue' in st.session_state.df_cleaned.columns and 'total_revenue' in st.session_state.df_cleaned.columns:
            # Convert 'Date' column to datetime and group by month
            st.session_state.df_cleaned['Date'] = pd.to_datetime(st.session_state.df_cleaned['Date'], dayfirst=True)
            
            # Select only numeric columns for resampling
            numeric_cols = st.session_state.df_cleaned.select_dtypes(include=[np.number]).columns
            monthly_data = st.session_state.df_cleaned.resample('ME', on='Date')[numeric_cols].mean()

            plt.figure(figsize=(12, 6))
            plt.plot(monthly_data.index, monthly_data['total_revenue'], color='orange', label='Total Revenue')
            plt.plot(monthly_data.index, monthly_data['predicted_revenue'], color='blue', label='Predicted Revenue')

            plt.xlabel('Date')
            plt.ylabel('Revenue')
            plt.title('Total Revenue vs Predicted Revenue')
            plt.xticks(rotation=45)
            plt.legend()
            st.pyplot(plt)
        else:
            st.error("Predicted revenue or total revenue not available for plotting.")