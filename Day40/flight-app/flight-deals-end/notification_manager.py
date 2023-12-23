from twilio.rest import Client
import smtplib

TWILIO_SID = YOUR_SID
TWILIO_AUTH_TOKEN = YOUR_TOKEN
TWILIO_VIRTUAL_NUMBER = YOUR_NUMBER
TWILIO_VERIFIED_NUMBER = YOUR_NUMBER
my_email = YOUR_EMAIL
password = YOUR_PASSWORD


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, data, message):
        for user in data:
            email = user['email']
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email,
                                    msg=f"Subject:{"Flight Deal"}\n\n{message}".encode('utf-8'))



