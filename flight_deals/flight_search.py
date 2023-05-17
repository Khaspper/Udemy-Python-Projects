import requests
import os
from dotenv import load_dotenv
load_dotenv("/Users/khaspper/Documents/code/python/.env")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.TEQ_api_key = os.getenv("TEQ_api_key")
        self.TEQ_api_end = "https://api.tequila.kiwi.com/"
        self.header = {
            "apikey": self.TEQ_api_key
        }

    def get_city_code(self, city, sheet_data, index):
        get_parameter = {
            "term": city,
            "locale": "en-US",
            "location_types": "city"
        }
        response = requests.get(url=f"{self.TEQ_api_end}locations/query", params=get_parameter,
                                headers=self.header).json()
        city_code = response["locations"][0]["code"]
        put_parameters = {
            "sheet1": {
                "iataCode": city_code,
            }
        }
        sheet_data.put_data(put_parameters, index)

    def find_price(self, parameter):
        return requests.get(url=f"{self.TEQ_api_end}v2/search", params=parameter, headers=self.header).json()
        pass
