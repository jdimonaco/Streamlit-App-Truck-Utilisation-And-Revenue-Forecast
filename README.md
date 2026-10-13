# Task Explanation

This project aims to analyse daily truck utilisation and predict revenue using Python, delivered through a Streamlit web app. The implementation uses pandas for data manipulation, scikit-learn for machine learning, and Streamlit for web app deployment. The project automates truck utilisation calculations, reducing manual input, and forecasts revenue to support better planning and decision-making. The goal is to optimise operations, reduce costs, and enhance financial forecasting. By providing these features through a web app, the project improves efficiency and empowers users to make data-driven decisions.

## Model Architecture

The model architecture involves the following steps:

### Data Preprocessing

* Handle missing values
* Remove duplicate records

### Testing

* Test the values before and after data preprocessing

### Model Training

* Calculate truck utilisation using chargeable weight (the larger of actual weight and volume × 333 kg, a common road-freight convention)
* Split the data into training and testing sets
* Train the linear regression model on the training set

### Model Evaluation

* Evaluate the model's performance using Mean Absolute Error
* Visualise the difference between the model's predictions and actual values

On the test set, the model's Mean Absolute Error is about 75 per shipment, compared with about 114 when every shipment is predicted at the average revenue.

## Streamlit App

A Streamlit app is provided to interact with the model. This app allows users to:

* Upload their own dataset
* Preprocess the data
* Train the model
* Make predictions
* Visualise results

To run the app locally:

    pip install -r requirements.txt
    streamlit run app.py

## Main Files

* main.py: Central execution point that calls data cleaning and analysis
* data_cleaner.py: Handles data preprocessing
* fleet_analysis.py: Revenue prediction and utilisation analysis
* test.py: Unit tests and validation
* app.py: Streamlit web interface for interactive analysis

## Data

This project and dataset were created specifically for educational purposes. The data is fictional and may not reflect the full complexity of real-world scenarios.
