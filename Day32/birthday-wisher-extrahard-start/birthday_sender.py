import datetime
import datetime as dt
import pandas
import random
import smtplib

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file=file_path, mode="r") as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthdays_dict[today_tuple]["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="francismunnier@gmail.com", password="chtnghhnhkaxsuju")
        connection.sendmail(from_addr="francismunnier@gmail.com", to_addrs=birthdays_dict[today_tuple]["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
