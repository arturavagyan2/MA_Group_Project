import csv 
import os

from generate_data import generate_subscribers, generate_activities, generate_transactions, generate_payment_methods, generate_RFM_segmentation, generate_retention_strategies, generate_clv 

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
subscribers_data = generate_subscribers()
activities_data = generate_activities()
transactions_data = generate_transactions()
payment_methods_data = generate_payment_methods()
rfm_segmentation_data = generate_RFM_segmentation()
retention_strategies_data = generate_retention_strategies()
clv_data = generate_clv()


# Save data to CSV files
save_to_csv(subscribers_data, 'subscribers_data.csv')
save_to_csv(activities_data, 'activities_data.csv')
save_to_csv(transactions_data, 'transactions_data.csv')
save_to_csv(payment_methods_data, 'payment_methods_data.csv')
save_to_csv(rfm_segmentation_data, 'rfm_segmentation_data.csv')
save_to_csv(retention_strategies_data, 'retention_strategies_data.csv')
save_to_csv(clv_data, 'clv_data.csv')

print("CSV files saved successfully in the 'csv_files' folder.")
