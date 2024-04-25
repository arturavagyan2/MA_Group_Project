import numpy as np
import pandas as pd
from ..db import SqlHandler
from lifelines import LogNormalAFTFitter

clv_handler = SqlHandler('subscription_database', 'transactions')

data = clv_handler.get_table_data()
clv_handler.close_cnxn()

connect_to_subscribers = SqlHandler('subscription_database', 'subscriber')

dim_customer = connect_to_subscribers.get_table_data()
connect_to_subscribers.close_cnxn()
dim_customer['survival_time_months'] = 1 + dim_customer['survival_time'] // 30

data['transaction_date'] = pd.to_datetime(data['transaction_date'])


def MM():
    """
    Calculate the average monthly margin based on the last year's transaction data.

    Returns:
    -------
    float:
        The calculated average monthly margin.
    """

    prev_year = data['transaction_date'].dt.year.max()-1
    filtered_data = data[data['transaction_date'].dt.year == prev_year]

    average_monthly_margin = np.sum(filtered_data['amount']) / 12

    return average_monthly_margin

def p():
    """
    Calculate the survival probabilities for customers using AFT estimator for a year.

    Returns:
    --------
    Dataframe:
        A dataframe of survival probabilities at different time points up to 12 months for each customer.
    """
    data = dim_customer.copy()
    data.drop(columns=['first_transaction_date', 'last_transaction_date'], inplace=True)
    data = pd.get_dummies(data, columns=['gender'], prefix='gender', drop_first=True)


    log_aft = LogNormalAFTFitter()
    log_aft.fit(data, duration_col="survival_time_months", event_col="event_observed")
    time_points = list(range(1, 13))
    pred = log_aft.predict_survival_function(data, times=time_points)


    return pred