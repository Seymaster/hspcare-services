"""
mail.py: This integrates the third-party API and receives data from Db as well as the email-recipient
"""


import requests
from Services.medlog.bookid import generate_random_number



def send_email(from_db,recipient):
    url = "https://services-staging.tm30.net/3ps/v1/services"
    bookid = generate_random_number()
    subject = f"{from_db} you just made a booking, booking ID: {bookid}"
    html = f"{from_db} Your order for booking with booking number: {bookid} has been received"
    emailPayload = {
            "provider":"sendgrid",
            "subject":subject,
            "recipients":[recipient],
            "body":html
            }
    headers = {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
              'client-id': 'humber'
            }
    requests.request("POST", url, headers=headers, data = emailPayload)
