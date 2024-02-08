import json
import requests

secrets_file = "secrets.json"
key = "account"
sub_keys = ["API_KEY","ACCESS_TOKEN","REFRESH_TOKEN"]

def getSecret(secrets_file, key, *sub_keys):
    try:
       with open(secrets_file) as f:
            data = json.load(f)
            values = {}
            if key in data:
                for sub_key in sub_keys:
                    values[sub_key] = data[key].get(sub_key)
            else:
                print(f"Key '{key}' not found in the JSON data.")
            return values
    except Exception as e:
        print("Error: ", e)

loginCreds = getSecret(secrets_file, key, *sub_keys)

api_key, access_token, refresh_token = loginCreds["API_KEY"], loginCreds["ACCESS_TOKEN"], loginCreds["REFRESH_TOKEN"]

def getRefreshToken(refresh_token, api_key):
    url = "https://api.ecobee.com/token"
    payload = {
        "grant_type": "refresh_token",
        "code": refresh_token,
        "client_id": api_key,
    }
    response = requests.post(url, data=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None


token_response = getRefreshToken(refresh_token, api_key)

new_refresh_token = token_response["access_token"]
    
print(new_refresh_token)