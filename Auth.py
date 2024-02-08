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

# Example usage:
refresh_token_value = "your_refresh_token_here"
client_id_value = "your_client_id_here"
api_key_value = "your_api_key_here"

token_response = refresh_token(refresh_token_value, client_id_value, api_key_value)
print(token_response)

