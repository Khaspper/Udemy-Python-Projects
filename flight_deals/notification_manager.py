from datetime import datetime
from datetime import timedelta
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv("/Users/khaspper/Documents/code/python/.env")


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.TWILLIO_account_sid = os.getenv("twilio_account_sid")
        self.TWILLIO_auth_token = os.getenv("twilio_auth_token")
        self.notif = ""

    def send_message(self, dep_code, des_code, dep_city, des_city, flight_price, dep_date, nights_in_dest):
        client = Client(self.TWILLIO_account_sid, self.TWILLIO_auth_token)
        format_dep_date = datetime.strptime(dep_date.split("T")[0], "%Y-%m-%d")
        return_date = (format_dep_date + timedelta(days=int(nights_in_dest))).date().strftime("%m/%d/%Y")
        format_dep_date = format_dep_date.date().strftime("%m/%d/%Y")

        self.notif = f"Low price alert! only ${flight_price} to fly from {dep_city}-{dep_code} to " \
                     f"{des_city}-{des_code}, from {format_dep_date} to {return_date}."
        message = client.messages \
            .create(
            body=self.notif,
            from_=os.getenv("twilio_phone_num"),
            to=os.getenv("my_phone_num")
        )
        print(message.status)
        pass
    pass
