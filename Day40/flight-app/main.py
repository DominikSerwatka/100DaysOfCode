import requests

MY_TOKEN = YOUR_TOKEN
ENDPOINT = YOUR_ENDPOINT
headers = {
            "Authorization": MY_TOKEN,
        }

print("Welcome to Dominik's Flight Club.\nWE find the best flight deals and email you.")
user_first_name = input("What is your name?\n")
user_last_name = input("What is your last name?\n")
is_true = True
while is_true:
    user_email = input("What is email?\n")
    user_email_2 = input("Type your email once again.\n")
    if user_email == user_email_2:
        print("You are in the club!")
        is_true = False
    else:
        print("Emails are different try again")
        is_true = True

params = {
    "user": {
        "firstName": user_first_name,
        "lastName": user_last_name,
        "email": user_email,
    }
}
response = requests.post(url=ENDPOINT, json=params, headers=headers)
print("Your are in the club!")


