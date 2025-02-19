from datetime import date, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

flight_search = FlightSearch()
datamanager = DataManager()
sheet_data = datamanager.get_sheet_data()

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

    if cheapest_flight_today.price_today != "N/A" and cheapest_flight_today.price_today < city["lowestPrice"]:
        print(f"Lower price flight found to {city["city"]}!")
