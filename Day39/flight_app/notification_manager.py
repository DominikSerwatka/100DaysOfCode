from twilio.rest import Client
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight):
        self.account_sid = "your id"
        self.auth_token = "your token"
        self.number_from = "your number"
        self.number_to = "your number"
        self.flight = flight

    def send_message(self):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! Only£{self.flight.price} to fly from {self.flight.departure_city_name}"
                 f"-{self.flight.departure_airport_code} to {self.flight.arrival_city_name}-"
                 f"{self.flight.arrival_airport_code}"
                 f", from {self.flight.inbound_date} to {self.flight.outbound_date}.",
            from_=self.number_from,
            to=self.number_to
        )
        print(message.status)

