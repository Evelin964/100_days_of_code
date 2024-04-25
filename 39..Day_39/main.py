#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.




import os
import requests
import pandas as pd

info_found_in_sheet = "https://api.sheety.co/d227ad5bce98690ad95c1e66af319197/flightDeals/prices"


json_data_sheeety = requests.get(url=info_found_in_sheet).json()

dataframe_sheet = pd.json_normalize(json_data_sheeety["prices"])
#print(dataframe_sheet)

from flight_search import FlightSearch

flight_info = FlightSearch()
flight_data = flight_info.get_flight_info("Bucharest")
print(flight_data)

