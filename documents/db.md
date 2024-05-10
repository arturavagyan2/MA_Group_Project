# Database Documentation

## Overview
This documentation covers the data generation, manipulation, and schema details of the SuRFM package which utilizes an SQLite database to store and manage subscriber data and associated activities.

## Data Generation
The data generation scripts use the `Faker` library to create realistic mock data for subscribers, activities, transactions, payment methods, RFM segmentation, retention strategies, and customer lifetime value (CLV).

### Key Functions
- `generate_subscribers()`: Generates mock subscriber data.
- `generate_activities()`: Generates activities related to subscribers.
- `generate_transactions()`: Generates financial transactions of subscribers.
- `generate_payment_methods()`: Creates a list of payment methods.
- `generate_RFM_segmentation()`: Generates RFM scores for subscribers.
- `generate_retention_strategies()`: Creates retention strategies based on RFM segments.
- `generate_clv()`: Computes the Customer Lifetime Value for subscribers.

## Saving Data to CSV
Data generated from the above functions can be stored in CSV format using the `save_to_csv(data, filename)` function, which checks if required CSV files exist and writes data accordingly.

## Database Schema
The database schema is defined using SQLAlchemy ORM and includes the following entities:
- `Subscriber`
- `Activity`
- `Transaction`
- `PaymentMethod`
- `RFMSegmentation`
- `RetentionStrategy`
- `CLV`

### Relationships
- Each `Subscriber` has multiple `Activities`, `Transactions`, and can have one `RFMSegmentation` and one `CLV`.
- Each `Transaction` is linked to a `PaymentMethod`.
- Each `RFMSegmentation` is linked to one `RetentionStrategy`.

## SQL Operations
The `SqlHandler` class is used to manage database interactions. Key methods include:
- `insert_many(df)`: Inserts data from a DataFrame into the specified table.
- `get_table_data(columns, condition)`: Retrieves data from a table based on the specified columns and conditions.
- `update_table(set_clause, condition)`: Updates rows in a table based on the given condition.
- `truncate_table()`: Deletes all data from a table.
- `close_cnxn()`: Closes the database connection.

## RFM Data Handling
- `get_rfm_data()`: Fetches RFM data for segmentation.
- `segment_subscribers(rfm_data)`: Segments subscribers based on their RFM scores.
- `get_declining_customers(rfm_data)`: Identifies declining customers based on their RFM scores.

## Additional Functionalities
- `get_email_by_subscriber_id(subscriber_id)`: Retrieves the email of a subscriber by their ID.
- `update_subscriber_emailSent_status(subscriber_id, email_sent)`: Updates the email sent status for a subscriber.

## Installation and Setup
Ensure all required packages are installed and Python is properly configured to interact with the SQLite database. For detailed setup instructions, refer to the main README.md of the SuRFM package.
