import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.107883
MY_LONG = 17.038538
iss_latitude = 0
iss_longitude = 0


def get_iss_poss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    global iss_longitude, iss_latitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


def is_visible():
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        if MY_LONG-5 <= iss_longitude <= MY_LONG+5:
            print("You can see it")
            return True
    print("You can't see it")
    return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
sunrise = 0
sunset = 0


def get_sun():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    global sunrise, sunset
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def is_dark(sunset_hour, sunrise_hour):
    time_now = datetime.now()
    print(time_now.hour)
    time_now_hour = time_now.hour
    if time_now_hour < sunrise_hour or sunset_hour < time_now_hour:
        print("yes")
        return True
    print("No, it's day")
    return False


def send_email():
    my_email = "francismunnier@gmail.com"
    password = "chtnghhnhkaxsuju"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        topic = "iss"
        msg = "Look up to see iss"
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:{topic}\n\n{msg}")


while True:
    get_iss_poss()
    if is_visible():
        get_sun()
        if is_dark(sunset_hour=sunset, sunrise_hour=sunrise):
            send_email()
    time.sleep(60)




