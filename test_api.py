import requests
import time

'''
Make sure to test it with the server running. 
To run the server, navigate to SuRFM/api directory in the terminal, 
then type "uvicorn main:app" without the strings and hit enter.
'''

base_url = "http://localhost:8000"

# Test Case 1: Get subscriber information 
def test_get_subscriber_info(subscriber_id):
    response = requests.get(f"{base_url}/subscriber?id={subscriber_id}")
    print(response.json())
    time.sleep(1)

# Test Case 2: Add a new subscriber
def test_add_subscriber(subscriber_data):
    response = requests.post(f"{base_url}/new_subscriber", params=subscriber_data)
    print(response.status_code)
    print(response.json())
    time.sleep(1)

# Test Case 3: Update subscriber information
def test_update_subscriber(subscriber_id, updated_data):
    response = requests.put(f"{base_url}/update_subscriber?Subscriber_ID={subscriber_id}", params=updated_data)
    print(response.json())
    time.sleep(1)

'''
This is the data to create a new subscriber, where all the attributes mentioned are required.
'''
subscriber_data = {
        "name": "Hraaaaaa",
        "email": "hrag@gmail.com",
        "age": 20,
        "location": "Armenia",
        "gender": "Male"
    }

'''
This is the data to update the subscriber with their respective ID. 
In this case, the only updates are the Name, Subscribtion Ending and Event Observed.
Subscribtion_Ended takes [None, True] values, in case of True, the subscribtion is marked
as ended with the current date, and the Survival_time is calculated in the CSV file.

To update other attributes, add the correct attribute name to the keys in the dictionary below
with their respective values.
'''
updated_data = {
        "Name": "Hrag Sousani",
        "Subscribtion_Ended": True,
        "Event_Observed": True
    }

test_add_subscriber(subscriber_data) # To post (Create a new entry in the CSV file)
test_update_subscriber(101, updated_data) # To Put (Update the entry with the mentioned ID)
test_get_subscriber_info(101) # To Get (Get the entry data with the mentioned ID)
