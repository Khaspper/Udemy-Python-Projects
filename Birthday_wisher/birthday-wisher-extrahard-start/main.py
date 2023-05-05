import smtplib
import pandas
import datetime as dt
import random

# * Making the email
my_email = "thrwawaylala@gmail.com"
password = "tyzgzcbarwftdadi"

# * Get the data from the csv file
birthdays = pandas.read_csv("birthdays.csv").to_records()

# * Get the date of right now
now_dt = dt.datetime.now()

# * Loop through the array and check if there is anyone with the same month and day as the current date
for _ in range(len(birthdays)):
    if (birthdays[_]["month"] == now_dt.month) and birthdays[_]["day"] == now_dt.day:
        with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as letter_format:
            letter = letter_format.read().replace("[NAME]", birthdays[_]["name"])
        # * Sending the email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthdays[_]["email"],
                                msg=f"Subject: Happy Birthday!!!\n\n{letter}")
