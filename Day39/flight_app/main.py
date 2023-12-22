#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.all_data()
for item in sheet_data['prices']:
    if item["iataCode"] == '':
        flight_search = FlightSearch()
        code = flight_search.get_iata_code(item['city'])
        data_manager.update_row(id=item['id'], code=code)
        flight_search = FlightSearch()
        flight = flight_search.get_flight_data(fly_from="LON", fly_to=code)
    else:
        flight_search = FlightSearch()
        flight = flight_search.get_flight_data(fly_from="LON", fly_to=item['iataCode'])

    if flight.price < item['lowestPrice']:
        print("Cheep flight")
        notify = NotificationManager(flight)
        notify.send_message()





