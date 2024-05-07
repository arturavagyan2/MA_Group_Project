import os
import pandas as pd
from SuRFM.db.sql_handler import SqlHandler

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define mapping dictionary for table names and relative file paths
table_file_mapping = {
    'subscriber': './csv_files/subscribers_data.csv',
    'activity': './csv_files/activities_data.csv',
    'transactions': './csv_files/transactions_data.csv',
    'payment_method': './csv_files/payment_methods_data.csv',
    'rfm_segmentation': './csv_files/rfm_segmentation_data.csv',
    'retention_strategy': './csv_files/retention_strategies_data.csv',
    'clv': './csv_files/clv_data.csv'
}

# Construct absolute paths from relative paths and insert data for each table
for table, relative_file_path in table_file_mapping.items():
    absolute_file_path = os.path.join(current_dir, relative_file_path)
    handler = SqlHandler('subscription_database', table)
    data = pd.read_csv(absolute_file_path)
    handler.insert_many(data)
    handler.close_cnxn()
