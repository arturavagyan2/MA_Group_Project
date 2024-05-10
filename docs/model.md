# Model Documentation

## Overview
This documentation describes the Customer Lifetime Value (CLV) model used in the SuRFM package, detailing the processes of calculating recency, frequency, monetary (RFM) values, and the survival probabilities to estimate CLV.

## CLV Model Components

### CLV Class (`clv.py`)
The `CLV` class is responsible for calculating the Customer Lifetime Value based on the customer's transaction history and their survival probabilities. It uses methods to calculate RFM values and then applies these to compute the CLV.

#### Key Methods
- `calculate_rfm()`: Calculates the Recency (days since last transaction), Frequency (number of transactions), and Monetary (total transaction amount) values for a specific customer.
- `calculate_clv()`: Calculates the CLV by considering discount rates, survival probabilities, and monthly margins.

### Data Processing (`data_processing.py`)
This script handles data retrieval and processing required for CLV calculations, including the computation of average monthly margins and survival probabilities using lifeline's LogNormalAFTFitter.

#### Key Functions
- `MM()`: Computes the average monthly margin from the last year's transaction data.
- `p()`: Estimates survival probabilities for each customer for up to 12 months using a log-normal accelerated failure time model.

## Database Interactions
Both scripts interact with the database using the `SqlHandler` class to retrieve necessary data:
- Transaction data and subscriber data are fetched and processed to calculate RFM values and survival probabilities.
- Database connections are managed to ensure efficient data retrieval and processing.

## Usage
1. **RFM Calculation**: Initiate an instance of the `CLV` class by passing a DataFrame containing customer transaction data, a specific customer ID, and the number of months (`t`) for which the CLV is calculated.
2. **CLV Calculation**: Call the `calculate_clv()` method to receive the estimated CLV, which incorporates customer behavior patterns and their expected lifetime.

## Example
Here's a basic example of how you might use the CLV model within your application:

```python
import pandas as pd
from clv import CLV

# Assuming customer_data is a DataFrame containing all necessary transaction data
customer_id = 101
t = 12  # Calculate CLV for 12 months

clv_model = CLV(customer_data, customer_id, t)
clv_value = clv_model.calculate_clv()

print(f"The calculated CLV for customer {customer_id} over {t} months is: {clv_value}")
```

## Additional Notes
Ensure all dependencies are properly installed.
Adjust the model parameters and functions based on the specific requirements and data characteristics of your project.

