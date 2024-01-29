"""This is Day 32 of Python 30 days challenge from DR. Angela Yu course
This is a program that will send birthday wishes to your friends on their birthday.
"""
import smtplib 
import datetime as dt
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, to_email, is_html=False):
    """
    Sends an email with the specified subject, body, and recipient.

    Parameters:
    - subject (str): The subject of the email.
    - body (str): The body content of the email.
    - to_email (str): The email address of the recipient.
    - is_html (bool): Indicates whether the body content is HTML (default is False).

    Returns:
    None
    """
    from_email = ""
    from_password = ""
    
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
        motivational_line = file.readlines()
        pair = random.choice(motivational_line)
        owner = pair.split(" - ")[1]
        quote = pair.split(" - ")[0]
        
        return owner, quote




today = dt.datetime.now()
if today.weekday() == 0:
    owner, quote = get_quote_of_the_day()
    send_email(owner, quote, "oferteevelin1996@gmail.com")
