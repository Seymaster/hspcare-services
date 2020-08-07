"""
mail.py: This integrates the third-party API and receives data from Db as well as the email-recipient
"""


import requests
import json

def send_mail(from_db, recipient):
        url = "https://staging.api.humbergames.com/notifications/v1/email"
        subject = f"{from_db} just contacted us"
        html = f"{from_db} just contacted us"
        emailPayload = {
                "provider": "sendgrid",
                "subject": subject,
                "recipients": [
                        recipient
                        ],
                "header": {
                        "title": "The Email Header",
                        "bgColor": "",
                        "appName": "MyApp",
                        "appURL": "http://myapp.com",
                        "appLogo": "https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png"
                        },
                "content": html,
                "body": {
                        "content": "Inside Content: <br>Testing email content<br> <p>KKD</p>",
                        "greeting": "Greetings,",
                        "introLines": [
                        "Introduction Line",
                        "You can still add more intro"
                        ],
                        "outroLines": [
                        "1. Content below button",
                        "2. Still below button or rather main content"
                        ]
                }
        }
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'client-id': 'humber'
        }
        resp = requests.request("POST", url, headers=headers, data =json.dumps(emailPayload) )
        print(resp.text.encode('utf8'))