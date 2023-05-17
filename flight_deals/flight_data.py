from datetime import datetime
from datetime import timedelta


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.tomorrow = datetime.today() + timedelta(days=1)
        self.six_months = self.tomorrow.replace(month=self.tomorrow.month + 6)

    def get_cheap_flights(self, city_code, lowest_price, flight_search):
        parameter = {
            "fly_from": "LAS",
            "fly_to": city_code,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.six_months.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 14,
            "nights_in_dst_to": 20,
            "flight_type": "round",
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "partner_market": "us",
            "curr": "USD",
            "price_to": lowest_price,
            "sort": "price",
            "limit": 500,
            "select_stop_airport_exclude": False
        }
        response = flight_search.find_price(parameter)
        if response['_results'] != 0:
            return response["data"][0]
        return -1

    pass
