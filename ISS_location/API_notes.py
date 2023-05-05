import requests
import pandas
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json#")
# print(response)
# * When you print this out it gives you this <Response [200]>
# * The [200] is called the response code
# * They tell you if the request was successful or if it failed
# ! You can tell what each response code does!!!!
# * For example if the response code is the following (Where "XX" is the following numbers)
# * 1XX: Hold on something's happening this is not final
# * 2XX: Here you go everything went as expected you should be getting the data you expected
# * 3XX: Go away you don't have permission to get the data you are looking for
# * 4XX: You screwed up the thing youre looking for probably doesn't exist
# * 5XX: I screwed up meaning maybe the servers down
# response.raise_for_status()
#
# data = response.json()
#
# iss_longitude = data["iss_position"]["longitude"]
# iss_latitude = data["iss_position"]["latitude"]
#
# iss_position = (iss_longitude, iss_latitude)
# print(iss_position)

MY_LAT = 34.052235
MY_LONG = -118.243683

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
}

# * Make sure you read whether the API needs parameters or not
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)

now = dt.datetime.now()
print(now.hour)
