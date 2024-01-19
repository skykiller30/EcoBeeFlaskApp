# Collecting Temperature Readings from Multiple Devices
The purpose of the project is for beginners to to collect temperature data from multiple applications and place them all on 1 local dashboard.

# right now this is a work in progress with placeholder documents and code until I can get it all integrated into one python/Flask app

Temperature Data will be collected from:
- Google
- EcoBee
- Philips Hue

Each data source has its own method of collecting temperature see below on how to get started with each vendor

## EcoBee
(this requires an EcoBee Smart thermostat and an EcoBee account)
1. First create a developer account with EcoBee here [Become an EcoBee Developer](https://www.ecobee.com/home/developer/loginDeveloper.jsp)
2. After becoming a developer with EcoBee, an additional section will be available in account settings. Log into your EcoBee account and in the top right corner click on the user icon and a side bar menu should extend. Click on “Developer”
3. Click on “Create New” and enter your information. The Application Name has to be unique. Select “ecobee PIN” as the Authorization Method and click Save. After filling out information you will now have an “API Key” on the Name and Summary page. Copy this API Key
4. See getPIN.txt to get PIN. Replace API_KEY with your API key
5. See postPIN.txt to receive access token. Replace API_KEY with your API key and AUTHORIZATION_CODE with the authorization code you received from running getPIN.txt
6. See getRunTime.txt Replace ACCESS_TOKEN with your access token
