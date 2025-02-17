import os
from dotenv import load_dotenv
import requests
from datetime import datetime

#___________________________________GET CURRENT DATE/TIME _________________________________________#

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

#___________________________________GET ENV VARIABLES _____________________________________________#

load_dotenv(r"C:\fakepath\.env")
NUTRI_APP_ID = os.getenv("nutritionix_id")
NUTRI_API_KEY = os.getenv("nutritionix_api_key")
NUTRI_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.getenv("sheety_endpoint")
SHEETY_HEADERS = {"Authorization": os.getenv("sheety_token")}

GENDER = "YOUR_GENDER"
WEIGHT_KG = YOUR_WEIGHT
HEIGHT_CM = YOUR_HEIGHT
AGE = YOUR_AGE

#_________________________GET EXERCISE INFO USING NATURAL LANGUAGE QUERIES ________________________#

NUTRI_HEADERS = {
    "Content-Type": "application/json",
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

NUTRI_PARAMS = {
    "query": input("What exercises did you complete today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

nutri_response = requests.post(url=NUTRI_ENDPOINT, headers=NUTRI_HEADERS, json=NUTRI_PARAMS)
nutri_response.raise_for_status()
exercise_data = nutri_response.json()

#____________________ SAVE EXERCISE DATA INTO GOOGLE SHEETS USING SHEETY __________________________#

for exercise in exercise_data["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs, headers=SHEETY_HEADERS)
    sheety_response.raise_for_status()
    print(sheety_response.text)
