import os
import requests
from twilio.rest import Client


api_key = os.environ.get('API_KEY')
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = 'ACb3a857027b035b82a0af8215050f29c6'
auth_token = os.environ.get('AUTH_TOKEN')
MY_LAT = 51.107883
MY_LONG = 17.038538

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for item in data['list']:
    id = item['weather'][0]['id']
    if id <= 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_=os.environ.get('NUMBER1'),
        to=os.environ.get('NUMBER0')
    )
    print(message.status)
