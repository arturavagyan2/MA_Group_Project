from SuRFM.model import CLV
from SuRFM.db import SqlHandler
import pandas as pd

if __name__ == "__main__":

    connect_to_subscribers = SqlHandler('subscription_database', 'subscriber')

    subscribers = connect_to_subscribers.get_table_data()
    connect_to_subscribers.close_cnxn()

    subscribers['clv_value'] = [CLV(t=5, customer_id=id).calculate_clv() for id in subscribers['subscriber_id']]
    subscribers['clv_date'] = pd.Timestamp.now()  

    prediction = subscribers[['subscriber_id', 'clv_value', 'clv_date']].reset_index()
    prediction.rename(columns={'index': 'clv_id', 'subscriber_id': 'subscriber_id', 'clv_value': 'clv_value'}, inplace=True)

    labels = ["New Potential", "Emerging", "Established", "Champion"]
    prediction['predicted_type'] = pd.qcut(prediction['clv_value'], 4, labels=labels)

    prediction['is_success'] = prediction['predicted_type'].apply(lambda x: True if x == "Star" else False)

    connect_to_prediction = SqlHandler('subscription_database', 'clv')
    connect_to_prediction.insert_many(prediction.to_dict('records'))  
    connect_to_prediction.close_cnxn()
