"""This is Day 32 of Python 30 days challenge from DR. Angela Yu course
This is a program that will send birthday wishes to your friends on their birthday.
"""
import smtplib 
import datetime as dt
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_email, is_html=False):
        from_email = "oferteevelin1996@gmail.com"
        from_password = "rzhc ppom jqtz nnhs"
        
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))
        
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        try:
            server.starttls()
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
        except Exception as e:
            print(f'Failed to send email: {e}' )    
        finally:    
            server.quit()



def get_quote_of_the_day():
    with open("32.Day_32\quotes.txt") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
        return quote





quote = get_quote_of_the_day()
print(quote)

#send_email("Happy Birthday", "Happy Birthday Evelin", "oferteevelin1996@gmail.com")
