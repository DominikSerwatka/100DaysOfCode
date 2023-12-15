import smtplib
import datetime as dt
import random


def send_email(message, topic):
    my_email = "francismunnier@gmail.com"
    password = "chtnghhnhkaxsuju"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="francismunnier@gmail.com", msg=f"Subject:{topic}\n\n{message}")


# ---- read data  ---- #

with open(file="quotes.txt", mode="r") as file:
    quote = file.readlines()


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if day_of_week == 4:
    random_quote = random.choice(quote)
    send_email(message=random_quote, topic="Motivational quote")


