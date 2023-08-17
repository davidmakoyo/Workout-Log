import requests
from datetime import datetime

APP_ID = "4aeee0d2"
API_KEY = "42dcd227f82f8179de1ceb6b77d99e15"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

query = input("What exercise did you do today?\n")

params = {
    "query": query,
    "gender": "male",
    "weight_kg": 77.11,
    "height_cm": 182.88,
    "age": 19,
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)



USERNAME = "David"
PROJECT_NAME = "My-Workouts"
SHEET_NAME = "workouts"
AUTHORIZATION = "Bearer asdfasdfasdfasdfasdf"

sheety_endpoint = f"https://api.sheety.co/b987675314526c457d37a1677af2df18/myWorkouts/workouts"

now = datetime.now()
date = now.strftime("%m/%d/%Y")
time = now.strftime("%H:%M")

new_row = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": response.json()["exercises"][0]["user_input"],
        "duration": response.json()["exercises"][0]["duration_min"],
        "calories": response.json()["exercises"][0]["nf_calories"],
    }
}

sheety_headers = {
    'Content-Type': 'application/json',
    "Authorization": AUTHORIZATION,
}

sheety_response = requests.post(url=sheety_endpoint, json=new_row, headers=sheety_headers)
print(sheety_response.text)



