import requests
from instance.setins import sup_email
from Services.medlog.bookid import generate_random_number



def send_email(from_db):
    url = "https://services-staging.tm30.net/3ps/v1/services"
    sup_email = sup_email
    bookid = generate_random_number()
    subject = f"{from_db} you just made a booking, booking ID: {bookid}"
    html = f"{from_db} Your order for booking with booking number: {bookid} has been received"
    emailPayload = {
            "provider":"sendgrid",
            "subject":subject,
            "recipients":[sup_email],
            "body":html
            }
    headers = {
            'client_Id': '3TUxIEopcO3diIKs88uYEemWgvC4ja5ASsfDeqOQPUT4bi9wKBFX8YQ99G08BX3Nw9chw7jafDRmnAtsuCLxeTcLznytqxE8OLhkz4Q3bYBa5ZXoX2xrVNDE8SficsXXgkTXJZn9i9I1oeTFL7Yf0h8iuwc8yhLX63kGBcLHjcHfewWfj4izUck4Nh5YuCKTaH7UqScJLPcYn5YtGuBZC3A2gsNb9382WODWuOfBY9X9IlA30NR0c10q3dVAxzq4j94TisG2oSPmaaKpLPWSi8IdHXnson6Qhx9DhZxpvp53'
        }
    requests.request("POST", url, headers=headers, data = emailPayload)