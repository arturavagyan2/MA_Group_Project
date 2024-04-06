# Group 6 - Marketing Analytics Project for Streaming Services

## Project Objective

Our project aims to address the issue of declining customer retention and subscriber attrition of the aforementioned subscription-based companies and others alike by developing a Python package that will make use of RFM analysis, offering insights into behavior patterns, client segmentation, and their likelihood of churn.


## How It Works

1. **Data Input**: The package requires subscription data, including subscriber activity and transaction history.
2. **Analysis**: The RFM model segments subscribers based on their recency, frequency, and monetary value contributions to the service.
3. **Insights and Actions**: Based on the analysis, the package provides actionable insights for improving customer retention strategies.

# Step 1: Generate the data and fill the DB

## 1. How to generate the data
Inside RFM there is a db folder. Inside we have 4 files. First of all generate the data and run **save_to_csv.py** file to keep the generated files in csv format.

## 2. Construct the database
Run also the **schema.py** to activate the database. The empty tables will be available now in the subscription_database.db


## 3. Fill in the data
To move the generated data from the csv into the db just run the **basic_rfm.py** script.
