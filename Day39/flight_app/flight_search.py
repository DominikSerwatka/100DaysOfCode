import requests
from datetime import datetime, timedelta
from flight_data import FlightData


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.ENDPOINT_CODE = 'https://api.tequila.kiwi.com/locations/query'
        self.ENDPOINT_FLIGHT = 'https://api.tequila.kiwi.com/v2/search'
        self.API_KEY = "your api key"
        self.headers = {
            "apikey": self.API_KEY,
        }

    def get_iata_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=self.ENDPOINT_CODE, params=params, headers=self.headers)
        data = response.json()
        code = data["locations"][0]['code']
        return code

    def get_flight_data(self, fly_from, fly_to):

        date_from = datetime.now() + timedelta(days=1)
        date_to = date_from + timedelta(days=6*30)
        date_from = date_from.strftime("%d/%m/%Y")
        date_to = date_to.strftime("%d/%m/%Y")

        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            'ret_from_diff_city': False,
            "ret_to_diff_city": False,
            "curr": "GBP",
            "max_stopovers": 0,
            "one_for_city": 1,
        }
        response = requests.get(url=self.ENDPOINT_FLIGHT, headers=self.headers, params=params)
        data = response.json()
        flight_data = FlightData(price=data['data'][0]['price'], departure_city=data['data'][0]['cityFrom'],
                                 arrival_city=data['data'][0]['cityTo'], departure_airport=data['data'][0]['flyFrom'],
                                 arrival_airport=data['data'][0]['flyTo'],
                                 outbound_date=data['data'][0]["route"][0]["local_departure"],
                                 inbound_date=data['data'][0]["route"][1]["local_departure"])
        return flight_data





