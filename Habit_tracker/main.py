import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv("/Users/khaspper/Documents/code/python/.env")

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "mommymilfigger"
TOKEN = os.getenv("PIXELA_token")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_config = {
    "id": "graph1",
    "name": "Gym graph",
    "unit": "days",
    "type": "int",
    "color": "ajisai",
}

today = datetime(year=2023, month=5, day=11).strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "1"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today}"

# response = requests.put(url=graph_endpoint, json=pixel_data, headers=headers)
response = requests.delete(url=graph_endpoint, headers=headers)
print(response.text)


