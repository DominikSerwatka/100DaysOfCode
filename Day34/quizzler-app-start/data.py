import requests

def get_data():
    parameters = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    data = response.json()["results"]
    return data

question_data = get_data()

