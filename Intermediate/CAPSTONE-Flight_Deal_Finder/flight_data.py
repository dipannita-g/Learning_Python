class FlightData:

    def __init__(self, price, origin_city, destination_city, departure_date, return_date):

        self.price_today = price
        self.departure_airport = origin_city
        self.destination_airport = destination_city
        self.out_date = departure_date
        self.in_date = return_date

def find_cheapest_flight(flight_data):

    # Initialize FlightData Class with N/A values if JSON is empty or there are no flights

    if flight_data is None or not flight_data["data"]:
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")

    # Get first flight data

    first_flight = flight_data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    # Initialize FlightData Class with details of first flight in JSON data

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    # Compare remaining flights in JSON to first flight

    for flight in flight_data["data"]:

        price = float(flight["price"]["grandTotal"])

        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is £{lowest_price}")

    return cheapest_flight
