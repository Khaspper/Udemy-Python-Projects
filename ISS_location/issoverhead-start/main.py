import time

import requests
from datetime import datetime
import smtplib

MY_EMAIL = "thrwawaylala@gmail.com"
PASSWORD = "tyzgzcbarwftdadi"

MY_LAT = 34.052235
MY_LONG = -118.243683


def iss_is_around():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if ((MY_LAT - 5) <= iss_latitude <= (MY_LAT - 5)) and (MY_LONG - 5) <= iss_longitude <= (MY_LONG - 5):
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    sun_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    if sunset < time_now.hour or time_now.hour < sunrise:
        return True
    return False


while True:
    time.sleep(60)
    if iss_is_around() and is_dark:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="brandonnarciso24@gmail.com",
                                msg="Subject:ISS IS ABOVE\n\nLOOK UP!!!")
