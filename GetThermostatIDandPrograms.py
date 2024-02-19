import requests
import json


secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)

api_key = secrets_data["API_KEY"]
access_token = secrets_data["ACCESS_TOKEN"]
refresh_token = secrets_data["REFRESH_TOKEN"]
main_floor_id = None
upstairs_id = None
main_floor_file = "mainFloorBody.json"
upstairs_file = "upStairsBody.json"
ecoBeeDictionary = None


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
    return response

ecoBeeResponse = get_thermostat_data(access_token)

if ecoBeeResponse.status_code == 200:
    ecoBeeDictionary = ecoBeeResponse.json()

    def extract_identifiers(ecoBeeDictionary):
        for thermostat in ecoBeeDictionary["thermostatList"]:
            name = thermostat["name"]
            if name == "Main Floor":
                main_floor_id = thermostat["identifier"]
            elif name == "Upstairs":
                upstairs_id = thermostat["identifier"]
            else:
                print("There is no thermostats matching the names you've entered")
        return main_floor_id, upstairs_id
    main_floor_id, upstairs_id = extract_identifiers(ecoBeeDictionary)


    def build_post_body (main_floor_id, upstairs_id):
        main_floor_post_body = {}
        upstairs_post_body = {}
        for thermostat in ecoBeeDictionary["thermostatList"]:
            if thermostat["identifier"] == main_floor_id:
                main_floor_post_body["selection"] = {
                    "selectionType": "thermostats",
                    "selectionMatch": main_floor_id
                }
                main_floor_post_body["thermostat"] = {
                    "program": thermostat["program"]
                }
            elif thermostat["identifier"] == upstairs_id:
                upstairs_post_body["selection"] = {
                    "selectionType": "thermostats",
                    "selectionMatch": upstairs_id
                }
                upstairs_post_body["thermostat"] = {
                    "program": thermostat["program"]
                }
            else:
                print("Could not built post body content from JSON repsonse")
        return main_floor_post_body,upstairs_post_body
            
    main_floor_program_post,upstairs_program_post = build_post_body(main_floor_id,upstairs_id)
    #upstairs_post_post = build_post_body(upstairs_id)
    with open(main_floor_file, "w") as json_file:
        json.dump(main_floor_program_post, json_file)

    with open(upstairs_file, "w") as json_file:
        json.dump(upstairs_program_post, json_file)

    # Print identifiers
    print("Main Floor Identifier:", json.dumps(main_floor_program_post, indent=4))
    print("Upstairs Identifier:", json.dumps(upstairs_program_post, indent=4 ))

elif ecoBeeResponse.status_code == 500:
    print("Refresh Access Token")
else:
    print("Something went wrong", ecoBeeResponse)
    
#def get_thermostat_programs(main_floor_id, upstairs_id):
#    for thermostat in ecoBeeResponse["thermostatList"]:
#        if thermostat["identifier"] == main_floor_id:
#            main_floor_program = thermostat["program"]
#        elif thermostat["identifier"] == upstairs_id:
#            upstairs_program = thermostat["program"]
#        else: print("Could not find thermostats with that identifier")
#    return main_floor_program, upstairs_program

# main_floor_program, upstairs_program = get_thermostat_programs(main_floor_id,upstairs_id)