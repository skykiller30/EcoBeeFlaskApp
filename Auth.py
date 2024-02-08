import requests
import json

def refresh_token(refresh_token, client_id, api_key):
    url = "https://api.ecobee.com/token"
    payload = {
        "grant_type": "refresh_token",
        "code": refresh_token,
        "client_id": client_id,
        "client_secret": api_key
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


response = 
