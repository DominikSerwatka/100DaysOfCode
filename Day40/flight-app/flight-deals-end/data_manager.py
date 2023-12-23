from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = YOUR_SHEETY_PRICES_ENDPOINT
MY_TOKEN = YOUR_TOKEN
ENDPOINT = YOUR_ENDPOINT
headers = {
    "Authorization": MY_TOKEN,
}
SHEETY_USERS_ENDPOINT = YOUR_SHEETY_USERS_ENDPOINT


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)

    def get_user_data(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()
        print(data)
        self.destination_data = data["users"]
        return self.destination_data
