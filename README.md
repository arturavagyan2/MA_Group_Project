# Group 6 - Marketing Analytics Project for Streaming Services

## Project Objective

Our project aims to address the issue of declining customer retention and subscriber attrition of the aforementioned subscription-based companies and others alike by developing a Python package that will make use of RFM analysis, offering insights into behavior patterns, client segmentation, and their likelihood of churn.


## How It Works

1. **Data Input**: The package requires subscription data, including subscriber activity and transaction history.
2. **Analysis**: The RFM model segments subscribers based on their recency, frequency, and monetary value contributions to the service.
3. **Insights and Actions**: Based on the analysis, the package provides actionable insights for improving customer retention strategies.

# Step 1: Generate Data and Populate the Database

### 1. Data Generation Process
Navigate to the db folder within RFM. You'll find four files in there. Begin by generating the data using the provided tools. Run the save_to_csv.py script to store the generated data in CSV format.

### 2. Database Construction
Execute the schema.py script to initialize the database. This action creates empty tables within subscription_database.db.

### 3. Data Population
To transfer the generated data from CSV files into the database, run the basic_rfm.py script. This step fills the tables in the database with the relevant information.

Additional Notes:
* Make sure to have Python installed on your system.
* Ensure all dependencies are met before executing the scripts.
* For any issues or inquiries, feel free to reach out to the repository maintainers.
  
Have a greate time exploring the possibilities of our package! 📊✨
