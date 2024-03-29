# Run this once as part of Initial Set Up, or skip if you did example #1 on EcoBee's developer website and obtained all the secrets that way

import requests
import json
secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)
    
authorization_code = secrets_data["AUTHORIZATION_CODE"]
api_key = secrets_data["API_KEY"]

def get_access_token(authorization_code, api_key):
    url = "https://api.ecobee.com/token"
    payload = {
        "grant_type": "ecobeePin",
        "code": authorization_code,
        "client_id": api_key,
        
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None
    
token_response = get_access_token(authorization_code, api_key)
secrets_data.update({
    "ACCESS_TOKEN": token_response["access_token"],
    "REFRESH_TOKEN": token_response["refresh_token"]
})

with open(secrets_file, 'w') as file:
    json.dump(secrets_data, file, indent=4)