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
thermostat_list =thermostat_list.get("thermostatList", [])
#print("Successfull! Result:", json.dumps(thermostat_list, indent=4))

# Find the thermostat with name "Upstairs" and extract its identifier and program
upstairs_thermostat = next((thermostat for thermostat in thermostat_list if thermostat.get("name") == "Upstairs"), None)
upstairs_id = upstairs_thermostat.get("identifier") if upstairs_thermostat else None
upstairs_program = upstairs_thermostat.get("program", {}) if upstairs_thermostat else {}

# Convert the schedule of the upstairs thermostat to JSON string
upstairs_schedule = json.dumps(upstairs_program.get("schedule", {}))

# Extract climates of the upstairs thermostat
upstairs_climates = upstairs_program.get("climates", [])

# Find the thermostat with name "Main Floor" and extract its identifier and program
main_floor_thermostat = next((thermostat for thermostat in thermostat_list if thermostat.get("name") == "Main Floor"), None)
main_floor_id = main_floor_thermostat.get("identifier") if main_floor_thermostat else None
main_floor_program = main_floor_thermostat.get("program", {}) if main_floor_thermostat else {}

# Convert the schedule of the main floor thermostat to JSON string
main_floor_schedule = json.dumps(main_floor_program.get("schedule", {}))

# Extract climates of the main floor thermostat
main_floor_climates = main_floor_program.get("climates", [])

print(upstairs_id, json.dumps(upstairs_climates,indent=4))
