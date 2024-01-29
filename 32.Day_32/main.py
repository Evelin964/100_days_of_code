##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
import random
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from day_32 import send_email




def get_today():
    today = dt.datetime.now()
    return today.day, today.month

def get_birthdays():
    data = pd.read_csv("32.Day_32/birthdays.csv")
    birthdays = data.to_dict(orient="records")
    return birthdays




if __name__ == "__main__":
        
    file_contents = get_birthdays()

    for birthday_person in file_contents:
        if birthday_person["month"] == get_today()[1] and birthday_person["day"] == get_today()[0]:
            with open(f"32.Day_32/letter_templates/letter_{random.randint(1,3)}.txt") as file:
                letter = file.read()
                letter = letter.replace("[NAME]", birthday_person["name"])
                send_email("Happy Birthday", letter, birthday_person["email"])
                print("Email sent successfully")
            



