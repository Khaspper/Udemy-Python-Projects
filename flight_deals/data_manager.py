import requests
import os
from dotenv import load_dotenv
load_dotenv("/Users/khaspper/Documents/code/python/.env")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_AUTH = os.getenv("SHEETY_auth")
        self.SHEETY_endpoint = os.getenv("SHEETY_flightdeals_endpoint")
        self.SHEETY_headers = {
            "Authorization": self.SHEETY_AUTH
        }
        self.response = requests.get(url=self.SHEETY_endpoint, headers=self.SHEETY_headers).json()

    def get_data(self):
        return self.response

    def put_data(self, parameters, index):
        put_response = requests.put(url=f"{self.SHEETY_endpoint}/{index}", json=parameters, headers=self.SHEETY_headers)
        print(put_response.text)

    pass
