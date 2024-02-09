import requests
import json

secrets_file = "secrets.json"

with open(secrets_file) as f:
    secrets_data = json.load(f)

access_token = secrets_data["ACCESS_TOKEN"]