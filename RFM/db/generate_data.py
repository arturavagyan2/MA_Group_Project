import random

from faker import Faker
from datetime import timedelta

fake = Faker()

subscriber_ids = list(range(1, 101))
payment_method_ids = list(range(1, 6))

def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def generate_subscribers():
    for _ in subscriber_ids:
        return {
            'subscriber_id': _,
            'name': fake.name(),
            'email': fake.email(),
            'age': random.randint(18, 70),
            'gender': random.choice(['Male', 'Female', 'Other']),
            'location': fake.city(),
            'subscription_start_date': fake.date_time_this_decade(before_now=True, after_now=False),
            'subscription_end_date': fake.date_time_this_decade(before_now=False, after_now=True),
            'survival_time': random.randint(1, 365),
            'event_observed': fake.boolean()
        }

def generate_activities():
    for _ in range(200):  
        return {
            'activity_id': _,
            'subscriber_id': random.choice(subscriber_ids),
            'activity_type': fake.word(),
            'activity_date_time': fake.date_time_this_year(before_now=True, after_now=False)
        }

def generate_transactions():
    for _ in range(150):
        return {
            'transaction_id': _,
            'subscriber_id': random.choice(subscriber_ids),
            'transaction_date': fake.date_time_this_year(before_now=True, after_now=False),
            'transaction_amount': round(random.uniform(10.0, 500.0), 2),
            'payment_method_id': random.choice(payment_method_ids)
        }

def generate_payment_methods():
    for _ in payment_method_ids:
        return {
            'payment_method_id': _,
            'payment_name': fake.credit_card_provider()
        }

def generate_RFM_segmentation():
    for _ in range(1, 101): 
        return {
            'segment_id': _,
            'subscriber_id': random.choice(subscriber_ids),
            'recency_score': round(random.uniform(1, 5), 2),
            'frequency_score': round(random.uniform(1, 5), 2),
            'monetary_score': round(random.uniform(1, 5), 2),
            'segment_label': fake.word()
        }

def generate_retention_strategies():
    for _ in range(1, 21):
        return {
            'strategy_id': _,
            'segment_id': random.randint(1, 100),
            'strategy_name': fake.sentence(nb_words=4),
            'description': fake.text(),
            'performance_metrics': fake.word(),
            'status': random.choice(['Active', 'Inactive', 'Pending'])
        }

def generate_clv():
    for _ in range(1, 101):
        return {
            'clv_id': _,
            'clv_value': round(random.uniform(1000.0, 10000.0), 2),
            'clv_date': fake.date_time_this_year(before_now=True, after_now=False),
            'predicted_type': random.choice(['Optimistic', 'Pessimistic', 'Realistic']),
            'is_success': fake.boolean(),
            'subscriber_id': random.choice(subscriber_ids)
        }
