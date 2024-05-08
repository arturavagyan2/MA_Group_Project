# If package should be run based on the real data, the database shoulde be updated:

## HOW? Here are the steps: 

- put input files with exact these names into csv_files folder
        'subscribers_data.csv'
        'activities_data.csv'
        'transactions_data.csv'
        'payment_methods_data.csv'
        'rfm_segmentation_data.csv'
        'retention_strategies_data.csv'
        'clv_data.csv'

- make sure that csv files cooresponf to the ERD schema of the DB
- delete the *subscription_database.db* if there
- run *schema.py* inside the SuRFM/db to make new schema for your db
- run *basic_rfm.py* to fill the database