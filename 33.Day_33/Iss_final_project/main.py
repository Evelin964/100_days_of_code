import requests
from datetime import datetime
import sys
import os

send_email_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..", "32.Day_32"))
sys.path.append(send_email_folder)
from day_32 import send_email

MY_LAT = 0 # Your latitude
MY_LONG = 0 # Your longitude


def get_iss_position():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    return iss_latitude, iss_longitude

#Your position is within +5 or -5 degrees of the ISS position.

def sunset_sunrise(latitude, longitude):
    parameters = {
        "lat": latitude,
        "lng": longitude,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    return sunrise, sunset




def look_up():
    iss_latitude, iss_longitude = get_iss_position()
    sunrise, sunset = sunset_sunrise(MY_LAT, MY_LONG)
    if iss_latitude - 5 <= MY_LAT <= iss_latitude + 5 and iss_longitude - 5 <= MY_LONG <= iss_longitude + 5:
        if sunset <= datetime.now().hour <= sunrise:
            return True
    return False



def look_up_email():
    if look_up():
        
        send_email(subject="Look up!", body="The Iss is above you.", to_email="") 
    else:
        print("The ISS is not above you.")
        


if __name__ == "__main__":
            
    look_up_email()








#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



