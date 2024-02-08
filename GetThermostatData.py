import requests
import json

secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)

api_key = secrets_data["API_KEY"]
access_token = secrets_data["ACCESS_TOKEN"]
refresh_token = secrets_data["REFRESH_TOKEN"]


def get_thermostat_data(access_token):
    url = "https://api.ecobee.com/1/thermostat"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "format": "json",
        "body": '{"selection":{"selectionType":"registered","selectionMatch":""}}'
    }
    response = requests.get(url, headers=headers, params=params)

    ecoBeeResponse = response.json()
    
    if response.status_code == 200:
        return ecoBeeResponse
    elif response.status_code == 500 and "message" in ecoBeeResponse["status"] and "Authentication token has expired. Refresh your tokens." in ecoBeeResponse["status"]["message"]:
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
        new_access_token = token_response["access_token"]
        secrets_data["ACCESS_TOKEN"]=new_access_token
        with open(secrets_file, 'w') as file:
            json.dump(secrets_data, file, indent=4)
        return print("The access token has expired, but the secrets.json file has been updated with a new token. Please run again")
        
    else:
        print("Error:", response.status_code)
        return None

thermostat_data = get_thermostat_data(access_token)
secrets_data.update(thermostat_data)
with open(secrets_file, 'w') as file:
            json.dump(secrets_data, file, indent=4)
print(json.dumps(secrets_data, indent=4))
