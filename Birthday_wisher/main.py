import datetime as dt
import random
import smtplib


my_email = "thrwawaylala@gmail.com"
password = "tyzgzcbarwftdadi"

# * Getting the current day of the week
current_date_time = dt.datetime.now()
day_of_the_week = dt.datetime.weekday(current_date_time)

if day_of_the_week == 0:
    # * Making a list of the quotes
    with open("quotes.txt", mode="r") as quote_file:
        quotes = quote_file.readlines()

    random_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(to_addrs="thrwawaylala@yahoo.com",
                            from_addr=my_email,
                            msg=f"Subject:Weekly Quotes\n\n{random_quote}")
