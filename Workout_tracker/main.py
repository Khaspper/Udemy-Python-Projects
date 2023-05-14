import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("/Users/khaspper/Documents/code/python/.env")

NUTIX_post_endpoint = os.getenv("NUTIX_post_endpoint")
SHEETY_api_endpoint = os.getenv("SHEETY_api_endpoint")

NUTIX_APP_ID = os.getenv("NUTIX_app_id")
NUTIX_API_KEY = os.getenv("NUTIX_api_key")
SHEETY_AUTH = os.getenv("SHEETY_auth")

GENDER = "male"
WEIGHT_KG = 54.4311
HEIGHT_CM = 164.592
AGE = 21

NUTIX_headers = {
    "x-app-id": NUTIX_APP_ID,
    "x-app-key": NUTIX_API_KEY,
}

NUTIX_parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

SHEETY_headers = {
    "Authorization": SHEETY_AUTH
}

# ! Remember POST + JSON & GET + PARAMS
NUTIX_response = requests.post(url=NUTIX_post_endpoint, json=NUTIX_parameters, headers=NUTIX_headers)
NUTIX_result = NUTIX_response.json()

todays_date = datetime.now().strftime("%m/%d/%Y")
todays_time = datetime.now().strftime("%I:%M:%S %p")

for exercise in NUTIX_result["exercises"]:
    SHEETY_parameters = {
        "workout": {
            "date": todays_date,
            "time": todays_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    SHEETY_response = requests.post(url=SHEETY_api_endpoint, json=SHEETY_parameters, headers=SHEETY_headers)


# * Ran 5k and cycled for 20 minutes.
