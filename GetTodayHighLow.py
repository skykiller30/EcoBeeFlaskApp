import requests
import json
from datetime import datetime
import pytz

secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)

access_token = secrets_data["ACCESS_TOKEN"]
cst = pytz.timezone('America/Chicago')
today_date = datetime.now(cst).strftime('%Y-%m-%d')
temp_high = None
temp_low = None


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

    return response
   
    
#print(json.dumps(get_weather_data(access_token), indent=4))

ecoBeeResponse = get_weather_data(access_token)
if ecoBeeResponse.status_code == 200:
    ecoBeeResponse = ecoBeeResponse.json()
    for thermostat in ecoBeeResponse["thermostatList"]:
        for forecast in thermostat["weather"]["forecasts"]:
            if forecast["dateTime"].startswith(today_date):
                temp_high = forecast["tempHigh"]/ 10.0
                temp_low = forecast["tempLow"]/ 10.0
                break
        if temp_high and temp_low:
            break
    print("tempHigh for today",today_date,"is", temp_high)
    print("tempLow for today",today_date,"is", temp_low)
else:
    print("Error, probably need to refresh access token")