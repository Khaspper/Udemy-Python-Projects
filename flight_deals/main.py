from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

sheet_data = DataManager()
data = sheet_data.get_data()
flight_search = FlightSearch()
flight_data = FlightData()
send_notif = NotificationManager()

count = 1
for city in data["sheet1"]:
    count += 1
    if city["iataCode"] == "":
        flight_search.get_city_code(city["city"], sheet_data, count)
    cheap_flight = flight_data.get_cheap_flights(city["iataCode"], city["lowestPrice"], flight_search)
    if cheap_flight != -1:
        send_notif.send_message(cheap_flight["flyFrom"], cheap_flight["flyTo"], cheap_flight["cityFrom"],
                                cheap_flight["cityTo"], cheap_flight["price"],
                                cheap_flight["local_departure"], cheap_flight["nightsInDest"])
