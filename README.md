# Change EcoBee Comfort Settings
The purpose of the project is to build a Python/Flask App that runs on Docker. The app will adjust the temperature ranges of each Comfort Setting (Home, Away, Sleep, etc) based on the outdoor temperature. Cooler outdoor temperatures will create warmer indoor Comfort presents and hotter outside temperatures will create cooler indoor Comfort Settings. 

# Before this app can fly as a Docker/Flask app it must craw as some basic python scrips

- App will Authenicate with EcoBree and bring in bearer token.
- Query EcoBee API for thermostat and Forcast data
- If outside temperatures are too cold/too hot then the app will modify the existing comfort settings with new temperature presets
- change "samplesecrets.json" filename to "secrets.json"
- I will eventualy write a python setup script that will help with the initial EcoBee registration app but for right now just use Example #1 on [EcoBee's Developer Site](https://www.ecobee.com/home/developer/api/examples/ex1.shtml)


## EcoBee
(this requires an EcoBee Smart thermostat and an EcoBee account)
1. First create a developer account with EcoBee here [Become an EcoBee Developer](https://www.ecobee.com/home/developer/loginDeveloper.jsp)
2. After becoming a developer with EcoBee, an additional section will be available in account settings. Log into your EcoBee account and in the top right corner click on the user icon and a side bar menu should extend. Click on “Developer”
3. Click on “Create New” and enter your information. The Application Name has to be unique. Select “ecobee PIN” as the Authorization Method and click Save. After filling out information you will now have an “API Key” on the Name and Summary page. Copy this API Key
4. Go to Example #1 on [EcoBee's Developer Site](https://www.ecobee.com/home/developer/api/examples/ex1.shtml) and enter in your API key. After following the directions on Example 1 you should have an API KEY, ACCESS TOKEN and REFRESH TOKEN. These are the values you will enter in your samplesecrets.json file
