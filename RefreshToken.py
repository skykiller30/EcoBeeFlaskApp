import json
import requests

secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)

api_key = secrets_data["API_KEY"]
access_token = secrets_data["ACCESS_TOKEN"]
refresh_token = secrets_data["REFRESH_TOKEN"]

def getRefreshToken(refresh_token, api_key):
    url = "http://api.ecobee.com/token"
    payload = {
        "grant_type": "refresh_token",
        "code": refresh_token,
        "client_id": api_key,
    }
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        
        return response.json()
    else:
        print("Error:", response)
        return None
token_response = getRefreshToken(refresh_token, api_key)
new_access_token = token_response["access_token"]
secrets_data["ACCESS_TOKEN"]=new_access_token
with open(secrets_file, 'w') as file:
    json.dump(secrets_data, file, indent=4)