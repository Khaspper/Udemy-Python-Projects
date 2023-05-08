import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("/Users/khaspper/Documents/code/python/.env")
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = os.getenv("OWM_api_key")
account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")

weather_params = {
    "lat": "39.526901",
    "lon": "-119.813278",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages\
        .create(
        body="It's going to rain to day brody :)",
        from_=os.getenv("twilio_phone_num"),
        to=os.getenv("my_phone_num")
    )
    print(message.status)
