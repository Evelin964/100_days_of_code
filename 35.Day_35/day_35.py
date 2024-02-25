"""This is day 35 challenge from Dr. angela Yu's course 100 days of python
This is a weather api weather data to txt msg using twilio api"""
import os
import requests
from twilio.rest import Client

LAT ='' # your latitude
LON ='' # your longitude
WILL_RAIN = False
API_KEY = os.getenv('Weather_data_api_key')
if not API_KEY:
    raise ValueError('No API Key provided')
params = {
    'lat': LAT,
    'lon': LON,
    'appid': API_KEY,
}
apiendpoint_timestampe = f'http://api.openweathermap.org/data/2.5/forecast?id=&appid={API_KEY}'
json_data_timestamp = requests.get(apiendpoint_timestampe,timeout=10,params=params).json()

for interval in json_data_timestamp['list']:
    if interval['weather'][0]['id'] < 700:
        WILL_RAIN = True
if WILL_RAIN:
    ACCOUNT_ID = os.getenv('Acc_id_twilio')
    AUTH_TOKEN = os.getenv('Auth_token_twilio')
    client = Client(ACCOUNT_ID,AUTH_TOKEN)
    message = client.messages \
                    .create(
                        body="Today will rain, Bring Umbrella!",
                        from_='Your Number Twilio',
                        to='Your phone number'
                    )

    print(message.status)
