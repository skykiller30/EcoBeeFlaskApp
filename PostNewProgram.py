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
        "body": '{"selection":{"selectionType":"registered","selectionMatch":"","includeProgram":true}}'
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

thermostat_list = get_thermostat_data(access_token)

#if day high is above 70, apply cooler temperature ranges 
for thermostat in get_thermostat_data['thermostatList']:
    # Update coolTemp to 760
    for climate in thermostat['program']['climates']:
        climate['coolTemp'] = 760
