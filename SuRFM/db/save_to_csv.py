import csv
import os
from .generate_data import generate_subscribers, generate_activities, \
    generate_transactions, generate_payment_methods, \
    generate_RFM_segmentation, generate_retention_strategies, generate_clv


def save_to_csv(data, filename):
    with open(os.path.join('csv_files', filename), 'w', newline='') as csvfile:
        fieldnames = data[0].keys() if data else []
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for record in data:
            writer.writerow(record)


# Create a folder named 'csv_files' if it doesn't exist
folder_name = 'csv_files'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)


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

# Save data to CSV files using for loop
for filename, generator_function in data_generators.items():
    data = generator_function()
    save_to_csv(data, filename)

print("CSV files saved successfully in the 'csv_files' folder.")
