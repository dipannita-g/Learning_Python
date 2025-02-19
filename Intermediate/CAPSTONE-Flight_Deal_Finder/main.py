from datetime import date, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

flight_search = FlightSearch()
datamanager = DataManager()
sheet_data = datamanager.get_sheet_data()
notification_manager = NotificationManager()

#____________________________Update Google sheet if IATA codes are missing_________________________________#

city_iata_dict = {}

for item in sheet_data:
    city_name = item["city"]
    if item["iataCode"] == "":
        iata_code = flight_search.get_iata_code(city_name)
        city_iata_dict[city_name] = iata_code

datamanager.update_destination_codes(city_iata_dict)

#_____________________________________________Search for flights___________________________________________#

today = date.today()
departure_date = today + timedelta(days=1) # Tomorrow
return_date = today + timedelta(days=(2*7)) # 2 weeks from now

ORIGIN_CITY_IATA = "LON"

for city in sheet_data:

    DESTINATION_IATA = city["iataCode"]

    flight_info = flight_search.get_flight_info(
        origin_city=ORIGIN_CITY_IATA,
        destination_city= DESTINATION_IATA,
        departure_date=departure_date,
        return_date=return_date
    )

    cheapest_flight_today = find_cheapest_flight(flight_info)

    # ________________________Whatsapp if price lower than historical low price______________________________#

    if cheapest_flight_today.price_today != "N/A" and cheapest_flight_today.price_today < city["lowestPrice"]:
        print(f"Lower price flight found to {city["city"]}!")

        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight_today.price_today} to fly "
                         f"from {cheapest_flight_today.departure_airport} "
                         f"to {cheapest_flight_today.destination_airport}, "
                         f"on {cheapest_flight_today.out_date} "
                         f"until {cheapest_flight_today.in_date}."
        )
