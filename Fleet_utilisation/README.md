# Task Explanation

This project aims to analyse daily truck utilisation and predict revenue using Python. The implementation uses pandas for data manipulation (McKinney, 2010), scikit-learn for machine learning (Shukla, 2023), and Streamlit for web app deployment (Streamlit, 2020). The project seeks to automate the calculation of truck utilisation, reducing manual input, and to forecast revenue. The aim is to optimise operations, reduce costs, and enhance financial forecasting for better planning and decision-making, ultimately improving overall efficiency.


# Software Development Lifecycle (SDLC)

Planning: Define project scope, deliverables, milestones, and timelines. 

Requirement: Address challenges of truck utilisation and revenue prediction, including handling missing values, removing duplicates, calculating daily utilisation, and developing a prediction model.

Design: Develop methods to meet requirements. A DataCleaner and FleetAnalysis classes will encapsulate data processing and revenue prediction. Additionally, a user-friendly interface layout will be designed to facilitate user interactions.

Implementation: Develop code to implement the solution,integrating with Streamlit to ensure a seamless user interface for data input and retrieving prediction.

Testing: Verify each method’s functionality and overall prediction accuracy, checking for remaining missing values, duplicate shipment IDs, and evaluating the prediction model’s accuracy using metrics like Mean Absolute Error (MAE).

Deployment: Use Streamlit to create an interactive web application, allowing users to input data and obtain predictions.

Maintenance: Provide regular updates and improvements will be based on user feedback and new data.

# Using Large Language Models (LLMs)


The use of LLM was crucial in building a Streamlit app, debugging code, especially for graph creation with date column issues, and visualising aggregated data clearly. It also helped me understand how and why to initialise session state variables in app.py, which was challenging due to Streamlit’s logic limitations. This guidance was essential for overcoming technical challenges and improving the app’s functionality.


# References: 

1. McKinney, W. (2010) Data Structures for Statistical Computing in Python. Available at: https://pandas.pydata.org/ (Accessed: 28 October 2024).

2. Shukla, S. (2023) Exploring Scikit-learn: A Powerful Tool for Machine Learning. Available at: https://medium.com/@shuklashubh818/exploring-scikit-learn-a-powerful-tool-for-machine-learning-c86c03a7f10f (Accessed: 30 October 2024).

2. Streamlit (2020) Streamlit: The fastest way to build and share data apps. Available at: https://streamlit.io/ (Accessed: 28 October 2024).


# Data

This project and dataset were created specifically for educational purpose. The data is fictional and may not reflect the full complexity of real-world scenarios.

