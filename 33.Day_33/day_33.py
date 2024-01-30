import requests
import datetime as dt


# ---------------------------- CONSTANTS ------------------------------- #

MY_LAT = 44.426765  # Your latitude
MY_LONG = 26.102537  # Your longitude

def get_sunset_sunrise():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    return sunrise_hour, sunset_hour


print(get_sunset_sunrise())
print(dt.datetime.now().hour)