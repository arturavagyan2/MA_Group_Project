import os
import csv
from generate_data import generate_subscribers, generate_activities, \
    generate_transactions, generate_payment_methods, \
    generate_RFM_segmentation, generate_retention_strategies, generate_clv


def save_to_csv(data, filename):
    with open(os.path.join('csv_files', filename), 'w', newline='') as csvfile:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for record in data:
            writer.writerow(record)


def check_files_exist(required_files):
    folder_name = 'csv_files'  # noqa E501
    if not os.path.exists(folder_name):
        print("'csv_files' folder does not exist. Please create the folder or provide the correct folder path.")  # noqa E501
        return False
    else:
        if len(os.listdir(folder_name)) == 1:
            # Generate data for each entity
            data_generators = {
                'subscribers_data.csv': generate_subscribers,
                'activities_data.csv': generate_activities,
                'transactions_data.csv': generate_transactions,
                'payment_methods_data.csv': generate_payment_methods,
                'rfm_segmentation_data.csv': generate_RFM_segmentation,
                'retention_strategies_data.csv': generate_retention_strategies,
                'clv_data.csv': generate_clv
            }

            # Save data to CSV files using a for loop
            for filename, generator_function in data_generators.items():
                data = generator_function()
                save_to_csv(data, filename)

            print("CSV files saved successfully in the 'csv_files' folder.")
            return True
        else:
            print("'csv_files' folder is not empty. Skipping CSV file generation.")  # noqa E501
            return True


# Example of how to use the function
required_files = [
    'subscribers_data.csv',
    'activities_data.csv',
    'transactions_data.csv',
    'payment_methods_data.csv',
    'rfm_segmentation_data.csv',
    'retention_strategies_data.csv',
    'clv_data.csv'
]

check_files_exist(required_files)
