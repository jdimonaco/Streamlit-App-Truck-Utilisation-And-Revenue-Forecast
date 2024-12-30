# Task Explanation
This project aims to analyse daily truck utilisation and predict revenue using Python, delivered through a Streamlit web app. The implementation uses pandas for data manipulation, scikit-learn for machine learning, and Streamlit for web app deployment. The project automates truck utilisation calculations, reducing manual input, and forecasts revenue to support better planning and decision-making. The goal is to optimise operations, reduce costs, and enhance financial forecasting. By providing these features using a web-app platform, the project improve efficiency and empower users to make data-driven decisions.

## Model Architecture

The model architecture involves the following steps:

## Data Preprocessing:

Handle missing values 
Remove duplicate records

## Testing: 

Test the values before and after data preprocessing

## Model Training:

* Calculate truck utilisation
* Split the data into training and testing sets
* Train the logistic regression model on the training set

## Model Evaluation:

* Evaluate the model's performance using Mean Absolute Error
* Visualise the difference between the model's predictions and actual values


A Streamlit app is provided to interact with the model. This app allows users to:

* Upload their own dataset
* Preprocess the data
* Train the model
* Make predictions
* Visualise results

## Main Files

* main.py: Central execution point that calls data cleaning and analysis
* data_cleaner.py: Handles data preprocessing
* fleet_analysis.py: Revenue prediction and utilisation analysis
* test.py: Unit tests and validation
* app.py: Streamlit web interface for interactive analysis

## Data
This project and dataset were created specifically for educational purpose. The data is fictional and may not reflect the full complexity of real-world scenarios.
