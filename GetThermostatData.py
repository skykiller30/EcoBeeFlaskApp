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
    return response

ecoBeeResponse = get_thermostat_data(access_token)