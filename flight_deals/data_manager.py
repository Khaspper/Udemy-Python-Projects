import requests
import os
from dotenv import load_dotenv
load_dotenv("/Users/khaspper/Documents/code/python/.env")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.email1 = ""
        self.email2 = ""
        self.last_name = ""
        self.first_name = ""
        self.SHEETY_AUTH = os.getenv("SHEETY_auth")
        self.SHEETY_endpoint_prices = "https://api.sheety.co/30d0aad523f8e37e3ed32b4feeb1cbce/flights/sheet1"
        self.SHEETY_endpoint_users = "https://api.sheety.co/30d0aad523f8e37e3ed32b4feeb1cbce/flights/sheet2"
        self.SHEETY_headers = {
            "Authorization": self.SHEETY_AUTH
        }
        self.response = requests.get(url=self.SHEETY_endpoint_prices, headers=self.SHEETY_headers).json()

    def get_data(self):
        return self.response

    def put_data(self, parameters, index):
        put_response = requests.put(url=f"{self.SHEETY_endpoint_prices}/{index}",
                                    json=parameters, headers=self.SHEETY_headers)
        print(put_response.text)

    def get_user_info(self):
        print("Welcome to Markus' Flight Club.\nWe find the best flight deals and email you.")
        self.first_name = input("What is your first name? ")
        self.last_name = input("What is your last name? ")
        self.email1 = input("What is your email? ")
        self.email2 = input("Type your email again. ")
        while self.email2 != self.email1:
            print("Emails don't match please try again.")
            self.email1 = input("What is your email? ")
            self.email2 = input("Type your email again. ")
        parameters = {
            "sheet2": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email1
            }
        }
        response = requests.post(url=self.SHEETY_endpoint_users, json=parameters, headers=self.SHEETY_headers)
        print(response)
    pass
