import requests
import os
from dotenv import load_dotenv

load_dotenv(r"C:\fakepath\.env")

class DataManager:

    def __init__(self):

        self.sheety_endpoint = f"{os.getenv("sheety_flight_endpoint")}/"
        self.sheety_headers = {"Authorization": os.getenv("sheety_flight_token")}
        self.sheet_data = {}

    def get_sheet_data(self):

        sheety_response = requests.get(url=self.sheety_endpoint,
                                       headers=self.sheety_headers
                                       )
        sheety_response.raise_for_status()
        self.sheet_data = sheety_response.json()["prices"]
        return self.sheet_data

    def update_destination_codes(self, city_iata_dict):

        for item in city_iata_dict:

            new_data = {
                "price": {
                    "iataCode": city_iata_dict[item]
                }
            }
            object_id = ""
            for objects in self.sheet_data:
                if objects["city"] == item:
                    object_id = objects["id"]

            response = requests.put(url=f"{self.sheety_endpoint}/{object_id}",
                                    json=new_data,
                                    headers=self.sheety_headers
                                    )
            response.raise_for_status()
            print(response.text)