import requests
from datetime import datetime
import smtplib
import time

EMAIL = "example@gmail.com"
PASSWORD = "examplepassword"

MY_LAT = 51.507351
MY_LONG = -0.127758

def iss_is_overhead():

    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_longitude = float(iss_response.json()["iss_position"]["longitude"])
    iss_latitude = float(iss_response.json()["iss_position"]["latitude"])
    # ISS is within +5 or -5 degrees from my location
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_dark():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Europe/London"
    }
    response_dusk_dawn = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_dusk_dawn.raise_for_status()
    data = response_dusk_dawn.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:

    time.sleep(60)

    if iss_is_overhead() and is_dark():

        with smtplib.SMTP("smtp.gmail.com", port=587) as server:

            server.starttls()
            server.login(user=EMAIL, password=PASSWORD)
            server.sendmail(
                from_addr=EMAIL,
                to_addrs=EMAIL,
                msg=f"Subject: ISS Overhead\n\nLook up at the sky!"
            )
