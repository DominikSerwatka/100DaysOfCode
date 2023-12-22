class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city, departure_airport, arrival_city, arrival_airport, outbound_date, inbound_date):
        self.price = price
        self.departure_city_name = departure_city
        self.departure_airport_code = departure_airport
        self.arrival_city_name = arrival_city
        self.arrival_airport_code = arrival_airport
        new_outbound_date = outbound_date.split("T")
        self.outbound_date = new_outbound_date[0]
        new_inbound_date = inbound_date.split("T")
        self.inbound_date = new_inbound_date

    def print(self):
        print(self.price)
        print(self.departure_city_name)
        print(self.departure_airport_code)
        print(self.arrival_city_name)
        print(self.arrival_airport_code)
        print(self.inbound_date)
        print(self.outbound_date)
