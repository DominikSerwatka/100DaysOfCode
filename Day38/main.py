import requests
from datetime import datetime
import os

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
TOKEN = os.environ.get('TOKEN')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ.get("SHEET_ENDPOINT")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

parameter = {
    "query": "ran 10 km",
}

headers_sheets = {
    "Authorization": f"{os.environ.get('MY_TOKEN')}",
}

user_data = input("Tell me which exercises you did: ")
parameter["query"] = user_data


response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=headers, data=parameter)
data = response.json()

for item in data['exercises']:
    exercise = item['name']
    duration = item['duration_min']
    calories = item['nf_calories']
    today = datetime.now().strftime("%d/%m/%Y")
    time = datetime.now().strftime("%H:%M:%S")
    parameters = {
        'workout': {
            "date": today,
            "time": time,
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    response_sheet = requests.post(url=SHEET_ENDPOINT, json=parameters, headers=headers_sheets)
    

































