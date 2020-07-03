from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Foreignlog,json
from Services.medlog.mail import send_email
from instance.setins import sup_email
import requests
import json



# middleware
parser = reqparse.RequestParser()


class Foreignlogapi(Resource):
    def get(self):
        return "Landing page for foreign logistics"

    def post(self):
        parser.add_argument("fullname", type=str ,required=True)
        parser.add_argument("dob", type=int,required=True)
        parser.add_argument("email", type=str,required=True)
        args = parser.parse_args()
        url = "https://services-staging.tm30.net/3ps/v1/services"
        if all([args.get(field, False) for field in ["fullname","dob","email"]]):
            foreignbook = Foreignlog(fullname = args["fullname"], dob = args["dob"], email = args["email"])
            foreignbook_json = foreignbook.json()
            try:
                db.session.add(foreignbook)
                db.session.commit()
                bookid = generate_random_number()
                subject = f"{foreignbook.fullname} you just made a booking, booking ID: {bookid}"
                html = f"{foreignbook.fullname} Your order for booking with booking number: {bookid} has been received"
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
                return {
                    "status": 200,
                    "message": "Booking successful",
                    "user"   : foreignbook_json
                    },200
            except IntegrityError:
                db.session.rollback()
                return {
                    "status": 200,
                    "message": "User already exists"
                },400
        return {"status": "BAD REQUEST"},404
