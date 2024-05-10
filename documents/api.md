# API Documentation

## Overview
This documentation details the endpoints available in the SuRFM FastAPI application which provides functions to manage and interact with subscriber data for streaming services. The API allows operations such as retrieving, adding, updating, and deleting subscriber information, along with specialized queries for declining and low-value subscribers.

## Setup
The API utilizes FastAPI and interacts with an SQLite database via SQLAlchemy. Ensure the following packages are installed:

- `fastapi`
- `sqlalchemy`
- `pydantic`
- `sendgrid`

## API Endpoints

### Home Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Description**: Displays a welcome message and provides a link to the API documentation.
- **Response**: A JSON object with a welcome message.

### Retrieve Subscriber
- **URL**: `/subscriber`
- **Method**: `GET`
- **Query Parameters**:
    - `id`: Integer, required, the ID of the subscriber to retrieve.
- **Description**: Fetches a subscriber's information by their ID.
- **Success Response**:
    - **Code**: 200
    - **Content**: Subscriber data
- **Error Response**:
    - **Code**: 404 (Not Found) or 500 (Internal Server Error) with error details.

### Add New Subscriber
- **URL**: `/new_subscriber`
- **Method**: `POST`
- **Description**: Adds a new subscriber to the database.
- **Body**:
    - `name`: String, required
    - `email`: Email string, required
    - `age`: Integer, required
    - `location`: String, required
    - `gender`: Enum ["Male", "Female", "Other"], optional
- **Success Response**:
    - **Code**: 200
    - **Content**: Confirmation message with subscriber ID.
- **Error Response**:
    - **Code**: 500 (Internal Server Error) with error details.

### Update Subscriber Information
- **URL**: `/update_subscriber`
- **Method**: `PUT`
- **Query Parameters**:
    - Subscriber details to be updated.
- **Description**: Updates existing subscriber details.
- **Success Response**:
    - **Code**: 200
- **Error Response**:
    - **Code**: 404 (Not Found) or 500 (Internal Server Error) with error details.

### Delete Subscriber
- **URL**: `/delete_subscriber`
- **Method**: `DELETE`
- **Query Parameters**:
    - `subscriber_id`: Integer, required, ID of the subscriber to delete.
- **Description**: Deletes a subscriber from the database.
- **Success Response**:
    - **Code**: 200
- **Error Response**:
    - **Code**: 404 (Not Found) or 500 (Internal Server Error) with error details.

### Declining Subscribers
- **URL**: `/declining_subscribers`
- **Method**: `GET`
- **Query Parameters**:
    - `from_email`: String, optional, email to send from if sending notifications.
    - `send_email`: Boolean, optional, flag to send emails to declining subscribers.
- **Description**: Retrieves subscribers who are considered to be declining based on specific criteria and optionally sends them an email.
- **Success Response**:
    - **Code**: 200
- **Error Response**:
    - **Code**: 500 (Internal Server Error) with error details.

### Low Value Subscribers
- **URL**: `/low_value_subscribers`
- **Method**: `GET`
- **Description**: Identifies subscribers who fall below a certain threshold of value.
- **Success Response**:
    - **Code**: 200
- **Error Response**:
    - **Code**: 500 (Internal Server Error) with error details.

## Additional Notes
Ensure Python is installed and all dependencies are met before executing scripts. For any issues or inquiries, reach out to the repository maintainers.

