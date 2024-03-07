"""This is a workout tracker that uses the nutritionix api to get 
the calories burned from a given exercise and then adds
it to a google sheet using the sheety api.
This is part of 100 days of code from Dr. AnGela Yu udemy course.
"""
import os
from datetime import datetime
import requests
API_KEY = os.getenv('APIKEYNUTRIX') # this is the nutrix api key
APLICATION_ID = os.getenv('NUTRIXAPIID') # this is the nutrix api id
AUTORIZATION_BEARER = os.getenv('SHEETYAPIBEARER') # this is the sheety api bearer token

todays_date = datetime.now().strftime("%d/%m/%Y")
todays_time = datetime.now().strftime("%H:%M:%S")
NATURAL_LANGUAGE_ENDPOINT = ('https://trackapi.nutritionix.com'
                             '/v2/natural/exercise')
ADD_ROW_ENDPOINT = ('https://api.sheety.co/538a25c862887c85e3c831f2d9d3f148'
'/workoutFile/workouts')

header = {
    'Authorization': AUTORIZATION_BEARER,
    'Content-Type': 'application/json'

}
header_nutrix = {
    'x-app-id': APLICATION_ID,
    'x-app-key': API_KEY,  
}
user_excercise = input("Tell me what exercises you did today: ")
excercise_body = {
    'query': user_excercise
}
response_excercise = requests.post(NATURAL_LANGUAGE_ENDPOINT,
                                 json=excercise_body,
                                 headers=header_nutrix,timeout=10).json()
exercise_name =response_excercise['exercises'][0]['name']
calories_exercise =response_excercise['exercises'][0]['nf_calories']
duration_exercise = response_excercise['exercises'][0]['duration_min']
body_to_add = {
    'workout': {"date": todays_date, 
                 "time": todays_time, 
                 "exercise": exercise_name, 
                 "duration": duration_exercise, 
                 "calories": calories_exercise}}

add_row_command = requests.post(ADD_ROW_ENDPOINT, json=body_to_add, headers=header,timeout=10)
if add_row_command.status_code == 200:
    print("Row added successfully")
