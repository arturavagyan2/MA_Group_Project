from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Subscriber(Base):
    __tablename__ = 'subscriber'

    subscriber_id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender = Column(String)
    location = Column(String)
    subscription_start_date = Column(DateTime)
    subscription_end_date = Column(DateTime)
    survival_time = Column(Integer)
    event_observed = Column(Boolean)
    activities = relationship('Activity', back_populates='subscriber')
    transactions = relationship('Transaction', back_populates='subscriber')
    rfm_segmentation = relationship('RFMSegmentation', back_populates='subscriber', uselist=False)
    clv = relationship('CLV', back_populates='subscriber', uselist=False)

class Activity(Base):
    __tablename__ = 'activity'

    activity_id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer, ForeignKey('subscriber.subscriber_id'))
    activity_type = Column(String)
    activity_date_time = Column(DateTime)
    subscriber = relationship('Subscriber', back_populates='activities')

class Transaction(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer, ForeignKey('subscriber.subscriber_id'))
    transaction_date = Column(DateTime)
    transaction_amount = Column(Float)
    payment_method_id = Column(Integer, ForeignKey('payment_method.payment_method_id'))
    subscriber = relationship('Subscriber', back_populates='transactions')
    payment_method = relationship('PaymentMethod')

class PaymentMethod(Base):
    __tablename__ = 'payment_method'

    payment_method_id = Column(Integer, primary_key=True)
    payment_name = Column(String)
    transactions = relationship('Transaction', back_populates='payment_method')

class RFMSegmentation(Base):
    __tablename__ = 'rfm_segmentation'

    segment_id = Column(Integer, primary_key=True)
    subscriber_id = Column(Integer, ForeignKey('subscriber.subscriber_id'))
    recency_score = Column(Float)
    frequency_score = Column(Float)
    monetary_score = Column(Float)
    segment_label = Column(String)
    subscriber = relationship('Subscriber', back_populates='rfm_segmentation')
    retention_strategy = relationship('RetentionStrategy', back_populates='rfm_segmentation', uselist=False)

class RetentionStrategy(Base):
    __tablename__ = 'retention_strategy'

    strategy_id = Column(Integer, primary_key=True)
    segment_id = Column(Integer, ForeignKey('rfm_segmentation.segment_id'))
    strategy_name = Column(String)
    description = Column(String)
    performance_metrics = Column(String)
    status = Column(String)
    rfm_segmentation = relationship('RFMSegmentation', back_populates='retention_strategy')

class CLV(Base):
    __tablename__ = 'clv'

    clv_id = Column(Integer, primary_key=True)
    clv_value = Column(Float)
    clv_date = Column(DateTime)
    predicted_type = Column(String)
    is_success = Column(Boolean)
    subscriber_id = Column(Integer, ForeignKey('subscriber.subscriber_id'))
    subscriber = relationship('Subscriber', back_populates='clv')

if __name__ == '__main__':
    engine = create_engine('sqlite:///subscription_database.db')  
    Base.metadata.create_all(engine)
