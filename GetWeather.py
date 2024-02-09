import requests
import json

secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)

access_token = secrets_data["ACCESS_TOKEN"]


def get_weather_data(access_token):
    url = "https://api.ecobee.com/1/thermostat"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "format": "json",
        "body": '{"selection":{"selectionType":"registered","selectionMatch":"","includeWeather":true}}'
    }
    response = requests.get(url, headers=headers, params=params)

    return response.json()
   
    
print(json.dumps(get_weather_data(access_token), indent=4))