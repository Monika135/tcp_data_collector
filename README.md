# TCP Data Collector Server

A backend service that receives device data over **TCP connections**, validates the data, and stores it in a database.  
The system supports **multiple simultaneous client connections** and provides APIs to retrieve stored records.

Built using:

- Python
- Flask
- SQLAlchemy
- SQLite

---

# Project Features

- TCP server that listens on a configurable port
- Accepts **multiple client connections simultaneously**
- Parses **JSON input from devices**
- Validates incoming device data
- Stores device records in a database
- REST API to fetch stored device records
- Graceful error handling for malformed inputs

---

---

# Setup Instructions

## 1. Clone the Repository

```bash
git clone <repository-url>
cd data_collection_handler
```

## 1. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Mac/Linux)
```

## 1. Install Dependencies
```bash
pip install -r requirements.txt
```

## 1. Configure Environment Variables
```bash
TCP_SERVER_HOST=0.0.0.0
TCP_SERVER_PORT=5000
SQLALCHEMY_DATABASE_URI=sqlite:///devices.db
```

## How to Run the TCP Server

```bash
Start the TCP server using:

python tcp_server.py

Expected output:

TCP Server listening on port 5000

The server will now accept multiple device connections simultaneously.

Incoming device data should be sent in JSON format:

{
  "device_id": "device_1",
  "card_id": "card_101"
}

```
## Flask Server
```bash
Start the Flask API: python app.py

API will run on:
http://localhost:5000
```

## How to Test the API
```bash
GET /v1/api/device_record

Example request:

http://localhost:5000/v1/api/device_record?device_id=device_1&no_of_records=10

Example response:

{
    "message": "Device records fetched successfully",
    "data": [
        {
            "id": 13,
            "device_id": "random_device",
            "card_id": "random_card",
            "timestamp": "2026-04-01T17:41:12.639321",
            "created_at": "2026-04-01T17:41:12.639321"
        }
    ],
    "status": true,
    "type": "success_message"
}
```

## Example using curl:
```bash
curl --location 'http://127.0.0.1:5000/v1/api/device_record/?device_id=random_device&no_of_records=10' \
--header 'accept: application/json'
```

## Database Schema
```bash
Table: device_cards
Column	          Type
id	            Integer
device_id	      String
card_id	        String
timestamp	      DateTime
created_at      DateTime
```



