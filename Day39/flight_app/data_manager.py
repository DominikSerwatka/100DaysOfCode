import requests
from pprint import pprint
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.MY_TOKEN = "your token"
        self.ENDPOINT = "your endpoint"
        self.headers = {
            "Authorization": self.MY_TOKEN,
        }

    def update_row(self, id, code):
        params = {
            "price": {
                "iataCode": code,
            }
        }
        response = requests.put(url=f"{self.ENDPOINT}/{id}", headers=self.headers, json=params)

    def add_row(self):
        params = {
            "price": {
                "city": "Athens"
            }
        }
        response = requests.post(url=self.ENDPOINT, headers=self.headers, json=params)

    def all_data(self):
        response = requests.get(url=self.ENDPOINT, headers=self.headers)
        return response.json()
