import requests
import json
secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)



def get_access_token(authorization_code, client_id, api_key):
    url = "https://api.ecobee.com/token"
    payload = {
        "grant_type": "ecobeePin",
        "code": authorization_code,
        "client_id": client_id,
        "client_secret": api_key
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None





