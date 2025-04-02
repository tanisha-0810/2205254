import requests
import json

registration_url = "http://20.244.56.144/evaluation-service/register"

registration_payload = {
    "email": "2205254@kiit.ac.in",  
    "name": "Tanisha Mukherjee",  
    "mobileNo": "6291590558",  
    "githubUsername": "tanisha-0810",
    "rollNo": "2205254",  
    "collegeName": "Kalinga Institute of Industrial Technology",
    "accessCode": "nwpwrZ"  
}

registration_headers = {'Content-Type': 'application/json'}

try:
    registration_response = requests.post(
        registration_url,
        headers=registration_headers,
        data=json.dumps(registration_payload)
    )

    registration_response.raise_for_status()

    registration_data = registration_response.json()

    print("Registration successful!")
    print(json.dumps(registration_data, indent=4))

    client_id = registration_data["clientID"]
    client_secret = registration_data["clientSecret"]

    print(f"clientID: {client_id}")
    print(f"clientSecret: {client_secret}")

    # After running this script, replace the placeholders below with the
    # clientID and clientSecret you receive.

    client_id = "YOUR_CLIENT_ID_HERE"
    client_secret = "YOUR_CLIENT_SECRET_HERE"
