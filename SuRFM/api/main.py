from fastapi import FastAPI, Query, HTTPException
import pandas as pd
from datetime import datetime
import csv

app = FastAPI()
subscribers_path = 'subscribers_data.csv'


@app.get("/subscriber")
async def get_subscriber_info(id: int):
    data = pd.read_csv(subscribers_path)
    subscriber = data[data.subscriber_id == id].to_dict('records')
    if not subscriber:
        raise HTTPException(status_code=404, detail=f"Subscriber not found with ID: {id}")
    return subscriber


@app.post("/new_subscriber")
async def add_subscriber(name: str, email: str, age: int, location: str, gender: str = Query(enum=["Male", "Female", "Other"])):
    data = pd.read_csv(subscribers_path)
    subscriber_id = len(data) + 1
    subscription_start_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    if subscriber_id in data['subscriber_id'].values:
        raise HTTPException(status_code=400, detail="Subscriber ID already exists")

    new_subscriber = {
        'subscriber_id': subscriber_id,
        'name': name,
        'email': email,
        'age': age,
        'gender': gender,
        'location': location,
        'subscription_start_date': subscription_start_date,
        'subscription_end_date': None,
        'survival_time': None,
        'event_observed': False
    }

    try:
        with open(subscribers_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=new_subscriber.keys())
            writer.writerow(new_subscriber)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to add subscriber: {str(e)}")

    return {"message": f"Subscriber added successfully with ID: {subscriber_id}"}
    


@app.put("/update_subscriber")
async def update_subscriber(Subscriber_ID: int, Name: str = Query(None), Email: str = Query(None), Age: int = Query(None), Location: str = Query(None), Gender: str = Query(None, enum=["Male", "Female", "Other"]), Subscribtion_Ended: bool = Query(None, enum=[True]), Event_Observed: bool = Query(False)):
    data = pd.read_csv(subscribers_path)
    subscriber_index = data[data['subscriber_id'] == Subscriber_ID].index
    if len(subscriber_index) == 0:
        raise HTTPException(status_code=404, detail=f"Subscriber not found with ID: {Subscriber_ID}")
    subscription_start_date = pd.to_datetime(data.at[subscriber_index[0], 'subscription_start_date'])

    if Name is not None:
        data.at[subscriber_index[0], 'name'] = Name
    if Email is not None:
        data.at[subscriber_index[0], 'email'] = Email
    if Age is not None:
        data.at[subscriber_index[0], 'age'] = Age
    if Location is not None:
        data.at[subscriber_index[0], 'location'] = Location
    if Gender is not None:
        data.at[subscriber_index[0], 'gender'] = Gender
    if Subscribtion_Ended is True:
        current_time = pd.to_datetime(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
        data.at[subscriber_index[0], 'subscription_end_date'] = current_time
        duration = current_time - subscription_start_date
        data.at[subscriber_index[0], 'survival_time'] = duration.days
    if Event_Observed is not None:
        data.at[subscriber_index[0], 'event_observed'] = Event_Observed
    
    data.to_csv(subscribers_path, index=False)

    return {"message": "Subscriber data updated successfully"}
    