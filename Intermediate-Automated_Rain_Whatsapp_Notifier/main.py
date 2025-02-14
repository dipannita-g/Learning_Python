import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(r"C:\fakepath\.env")

account_sid = os.getenv("twilio_account_sid")
auth_token = os.getenv("twilio_auth_token")
api_key = os.getenv("OWM_api_key")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
OWM_parameters = {"lat": "53.349804",
              "lon": "-6.260310",
              "cnt": 4,
              "appid": api_key
              }

weather_response = requests.get(OWM_endpoint, params=OWM_parameters)
weather_response.raise_for_status()
weather_data = weather_response.json()

weather_today = [hour["weather"][0]["id"] for hour in weather_data["list"]]

will_rain = False

for weather_id in weather_today:
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Bring an umbrella ☔",
        from_="whatsapp:+1XXXXXXXXXX",
        to="whatsapp:+44XXXXXXXXXX",
    )
    print(message.status)
