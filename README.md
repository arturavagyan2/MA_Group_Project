# SuRFM: Surfing the Subscribers RFM

## Group 6 - Marketing Analytics Project for Streaming Services

### Project Objective

Our project aims to address the issue of declining customer retention and subscriber attrition in subscription-based companies, particularly in the context of streaming services. We propose the development of a Python package named SuRFM, leveraging RFM analysis to offer insights into behavior patterns, client segmentation, and their likelihood of churn.

Find our project on [PyPi](https://pypi.org/project/SuRFM/).

## How It Works

1. **Data Input**: The SuRFM package requires subscription data, including subscriber activity and transaction history.
2. **Analysis**: The RFM model segments subscribers based on their recency, frequency, and monetary value contributions to the service.
3. **Insights and Actions**: Based on the analysis, SuRFM provides actionable insights for improving customer retention strategies.


## Step 1: Generate Data and Populate the Database

### 1. Data Generation Process

Navigate to the `db` folder within SuRFM. You'll find four files there. Begin by generating the data using the provided tools. Run the `save_to_csv.py` script to store the generated data in CSV format.

### 2. Database Construction

Execute the `schema.py` script to initialize the database. This action creates empty tables within `subscription_database.db`.

### 3. Data Population

To transfer the generated data from CSV files into the database, run the `basic_rfm.py` script. This step fills the tables in the database with the relevant information.


### Additional Notes:

- Make sure to have Python installed on your system.
- Ensure all dependencies are met before executing the scripts.
- For any issues or inquiries, feel free to reach out to the repository maintainers.
  
Have a great time exploring the possibilities of our package! 📊✨
