import random
import csv 

from faker import Faker
from datetime import timedelta

fake = Faker()

subscriber_ids = list(range(1, 101))
payment_method_ids = list(range(1, 6))

def generate_subscribers():
    subscribers_data = []
    for _ in subscriber_ids:
        start = fake.date_time_this_decade(before_now=True, after_now=False)
        end = fake.date_time_this_decade(before_now=False, after_now=True)
        subscriber = {
            'subscriber_id': _,
            'name': fake.name(),
            'email': fake.email(),
            'age': random.randint(18, 70),
            'gender': random.choice(['Male', 'Female', 'Other']),
            'location': fake.city(),
            'subscription_start_date': start,
            'subscription_end_date': end,
            'survival_time': (end - start).days,
            'event_observed': fake.boolean()
        }
        subscribers_data.append(subscriber)
    return subscribers_data

def generate_activities():
    generated_activities = []
    for _ in range(200):  
        activity =  {
            'activity_id': _,
            'subscriber_id': random.choice(subscriber_ids),
            'activity_type': fake.word(),
            'activity_date_time': fake.date_time_this_year(before_now=True, after_now=False)
        }
        generated_activities.append(activity)
    return generated_activities

def generate_transactions():
    generated_transactions = []
    for _ in range(150):
        transaction =  {
            'transaction_id': _,
            'subscriber_id': random.choice(subscriber_ids),
            'transaction_date': fake.date_time_this_year(before_now=True, after_now=False),
            'transaction_amount': round(random.uniform(10.0, 500.0), 2),
            'payment_method_id': random.choice(payment_method_ids)
        }
        generated_transactions.append(transaction)
    return generated_transactions

def generate_payment_methods():
    generated_methods = []
    for _ in payment_method_ids:
        method = {
            'payment_method_id': _,
            'payment_name': fake.credit_card_provider()
        }
        generated_methods.append(method)
    return generated_methods

def generate_RFM_segmentation():
    generated_segmentation = []
    for _ in range(1, 101): 
        segment =  {
            'segment_id': _,
            'subscriber_id': random.choice(subscriber_ids),
            'recency_score': round(random.uniform(1, 5), 2),
            'frequency_score': round(random.uniform(1, 5), 2),
            'monetary_score': round(random.uniform(1, 5), 2),
            'segment_label': fake.word()
        }
        generated_segmentation.append(segment)
    return generated_segmentation

def generate_retention_strategies():
    generated_strategies = []
    for _ in range(1, 21):
        strategy = {
            'strategy_id': _,
            'segment_id': random.randint(1, 100),
            'strategy_name': fake.sentence(nb_words=4),
            'description': fake.text(),
            'performance_metrics': fake.word(),
            'status': random.choice(['Active', 'Inactive', 'Pending'])
        }
        generated_strategies.append(strategy)
    return generated_strategies

def generate_clv():
    generated_clvs = []
    for _ in range(1, 101):
        clv =  {
            'clv_id': _,
            'clv_value': round(random.uniform(1000.0, 10000.0), 2),
            'clv_date': fake.date_time_this_year(before_now=True, after_now=False),
            'predicted_type': random.choice(['Optimistic', 'Pessimistic', 'Realistic']),
            'is_success': fake.boolean(),
            'subscriber_id': random.choice(subscriber_ids)
        }
        generated_clvs.append(clv)
    return generated_clvs
