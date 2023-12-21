import requests
from datetime import datetime
import os

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "dominikser"
TOKEN = os.environ.get('TOKEN_PIXELA')

user_params = {
    "token": "dfdjfhd4893bs1",
    "username": "dominikser",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
pixela_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"

graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}
#
# response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixela_records_quantity_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
new_date = today.strftime("%Y%m%d")
print(today)
print(new_date)

date_test = datetime(year=2023, month=12, day=20).strftime("%Y%m%d")
print(date_test)

record_params = {
    "date": date_test,
    "quantity": "15",
}

#
# response = requests.post(url=pixela_records_quantity_endpoint, json=record_params, headers=headers)
# print(response.text)

update_params = {
    "quantity": "4",
}

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_test}"


# response = requests.put(url=update_pixel_endpoint, json=update_params, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_test}"

respons = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(respons.text)











