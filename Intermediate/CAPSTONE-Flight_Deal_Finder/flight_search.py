import requests
import os
from dotenv import load_dotenv

load_dotenv(r"C:\fakepath\.env")

class FlightSearch:

    def __init__(self):

        self.amadeus_client_id = os.getenv("amadeus_flight_API_key")
        self.amadeus_client_secret = os.getenv("amadeus_flight_API_secret")

    def get_token(self):

        token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        token_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        token_data = {
            "grant_type": "client_credentials",
            "client_id": self.amadeus_client_id,
            "client_secret": self.amadeus_client_secret,
        }

        response = requests.post(token_url, headers=token_headers, data=token_data)
        response.raise_for_status()
        response_data = response.json()
        access_token = response_data.get("access_token")
        return access_token

    def get_iata_code(self, city_name):

        iata_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations"
        headers = {
            "Authorization": f"Bearer {self.get_token()}"
        }
        query = {
            "keyword": city_name,
            "subType": "AIRPORT",
        }
        iata_response = requests.get(
            url=iata_endpoint,
            headers=headers,
            params=query
        )
        print(f"Status code {iata_response.status_code}. Airport IATA: {iata_response.text}")

        try:
            code = iata_response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code

    def get_flight_info(self, origin_city, destination_city, departure_date, return_date):

        headers = {
            "Authorization": f"Bearer {self.get_token()}"
        }
        amadeus_flight_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers?"

        params = {
            "originLocationCode": origin_city,
            "destinationLocationCode": destination_city,
            "departureDate": departure_date,
            "returnDate": return_date,
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": 3
        }

        flight_response = requests.get(amadeus_flight_endpoint, params=params, headers=headers)

        if flight_response.status_code != 200:
            print(f"get_flight_info() response code for destination - {destination_city}: "
                  f"{flight_response.status_code}")
            print("Response body:", flight_response.text)
            return None

        flight_data = flight_response.json()
        return flight_data
