#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.




import os
import requests
import pandas as pd



json_data_sheeety = requests.get(url=info_found_in_sheet).json()

dataframe_sheet = pd.json_normalize(json_data_sheeety["prices"])
#print(dataframe_sheet)

from flight_search import FlightSearch

