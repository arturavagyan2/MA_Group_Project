import os
from fastapi import FastAPI, Query, HTTPException, Depends
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import SQLAlchemyError
from ..db.schema import Subscriber
from pydantic import EmailStr
from ..db.sql_handler import SqlHandler
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
SQLALCHEMY_DATABASE_URL = "sqlite:///subscription_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def show_message():
    return {'message': 'head to http://127.0.0.1:8000/docs/ to test the APIs'}


@app.get("/subscriber")
async def get_subscriber_info(id: int, db: Session = Depends(get_db)):
    try:
        subscriber = db.query(Subscriber).filter(Subscriber.subscriber_id == id).first()  # noqa: E501
        if not subscriber:
            raise HTTPException(status_code=404, detail=f"Subscriber not found with ID: {id}")  # noqa: E501
        return subscriber
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")  # noqa: E501


@app.post("/new_subscriber")
async def add_subscriber(name: str, email: EmailStr, age: int, location: str, gender: str = Query(enum=["Male", "Female", "Other"]), db: Session = Depends(get_db)):  # noqa: E501
    try:
        subscription_start_date = datetime.now()
        new_subscriber = Subscriber(name=name, email=email, age=age, location=location, gender=gender, subscription_start_date=subscription_start_date, event_observed=0, email_sent=None)  # noqa: E501
        db.add(new_subscriber)
        db.commit()
        db.refresh(new_subscriber)
        return {"message": f"Subscriber added successfully with ID: {new_subscriber.subscriber_id}"}  # noqa: E501
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding subscriber: {str(e)}")  # noqa: E501


@app.put("/update_subscriber")
async def update_subscriber(
    Subscriber_ID: int,
    Name: str = Query(None),
    Email: EmailStr = Query(None),
    Age: int = Query(None),
    Location: str = Query(None),
    Gender: str = Query(None, enum=["Male", "Female", "Other"]),
    Subscribtion_Ended: bool = Query(None, enum=[True]),
    Event_Observed: int = Query(None, enum=[0, 1]),
    email_sent: bool = Query(False, enum=[True]),
    db: Session = Depends(get_db)):  # noqa: E125

    try:
        subscriber = db.query(Subscriber).filter(Subscriber.subscriber_id == Subscriber_ID).first()  # noqa: E501
        if not subscriber:
            raise HTTPException(status_code=404, detail=f"Subscriber not found with ID: {Subscriber_ID}")  # noqa: E501

        if Name is not None:
            subscriber.name = Name
        if Email is not None:
            subscriber.email = Email
        if Age is not None:
            subscriber.age = Age
        if Location is not None:
            subscriber.location = Location
        if Gender is not None:
            subscriber.gender = Gender
        if Subscribtion_Ended is True:
            current_time = datetime.now()
            subscriber.subscription_end_date = current_time
            duration = current_time - subscriber.subscription_start_date
            subscriber.survival_time = duration.days
        if Event_Observed is not None:
            subscriber.event_observed = Event_Observed
        if email_sent is True:
            current_time = datetime.now()
            subscriber.email_sent = current_time

        db.commit()
        return {"message": "Subscriber data updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating subscriber: {str(e)}")  # noqa: E501


@app.delete("/delete_subscriber")
async def delete_subscriber(subscriber_id: int, db: Session = Depends(get_db)):
    try:
        subscriber = db.query(Subscriber).filter(Subscriber.subscriber_id == subscriber_id).first()  # noqa: E501
        if not subscriber:
            raise HTTPException(status_code=404, detail=f"Subscriber not found with ID: {subscriber_id}")  # noqa: E501

        db.delete(subscriber)
        db.commit()
        return {"message": f"Subscriber with ID {subscriber_id} has been deleted successfully"}  # noqa: E501
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting subscriber: {str(e)}")  # noqa: E501


@app.get("/declining_subscribers")
async def get_declining_subscribers():
    try:
        connect_to_rfm = SqlHandler('subscription_database', 'RFM_segmentation')
        rfm_data = connect_to_rfm.get_rfm_data()
        segmented_data = connect_to_rfm.segment_subscribers(rfm_data)
        declining_subscribers_df = connect_to_rfm.get_declining_customers(segmented_data)
        connect_to_rfm.close_cnxn()

        declining_subscribers = declining_subscribers_df.to_dict(orient='records')

        subject = "Your Subscription is at Risk"
        body = "Dear Subscriber,\n\nWe've noticed a decline in your engagement with our services, and we'd like to reach out to understand how we can better serve you. Please contact our support team for assistance.\n\nBest regards,\nThe Subscription Team" # noqa: E501

        print(declining_subscribers)
        for subscriber in declining_subscribers:
            subscriber_id = subscriber['subscriber_id']
            connect_to_subscribers = SqlHandler('subscription_database', 'subscriber')
            subscriber_info = connect_to_subscribers.get_email_by_subscriber_id(subscriber_id=subscriber_id)
            connect_to_subscribers.close_cnxn()
            if subscriber_info:
                email = subscriber_info
                try:
                    message = Mail(
                        from_email = 'hragsoussani4@gmail.com',
                        to_emails = email,
                        subject = subject,
                        plain_text_content = body
                    )
                    sg = SendGridAPIClient(SENDGRID_API_KEY)
                    print(email)
                    response = sg.send(message)
                    print(response.status_code)
                    if response.status_code == 202:
                        update_to_subscribers = SqlHandler('subscription_database', 'subscriber')
                        update_to_subscribers.update_subscriber_data(subscriber_id=subscriber_id, email_sent=True)
                        update_to_subscribers.close_cnxn()
                except Exception as e:
                    print(f"Error sending email to {email}: {e}")
        return declining_subscribers
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving declining subscribers: {str(e)}")
    



