import smtplib
import datetime as dt


my_email = "thrwawaylala@gmail.com"
# * CHECK YOUR SECURITY SETTINGS UNDER "app passwords"
password = "tyzgzcbarwftdadi"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="thrwawaylala@yahoo.com",
                        msg="Subject:Women\n\nI miss Nohemy!!!!!")


current_date_time = dt.datetime.now()

# * When this line execute this will be printed out
print(current_date_time)
# * 2023-05-04 18:57:35.043398
# * You can use current_date_time.year to print out the year etc

# * With this library you can also access the weekday like this

day_of_the_week = current_date_time.weekday()
print(day_of_the_week)
# * Right now it is thursday but remember that computers count by starting at 0 so monday is actually 0 instead of 1

# * This is how you create a datetime object
data_of_birth = dt.datetime(year=2002, month=3, day=24)
