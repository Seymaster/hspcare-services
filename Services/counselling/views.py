from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Counselling,json
from Services.medlog.mail import send_email
from instance.config import sup_email
import json

# middleware
parser = reqparse.RequestParser()


class Counselapi(Resource):
    def get(self):
        return "Landing page for Counselling"


    def post(self):
        parser.add_argument("fullname", type=str ,required=True)
        parser.add_argument("dob", type=int,required=True)
        parser.add_argument("email", type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["fullname","dob","email"]]):
            counselbook = Counselling(fullname = args["fullname"], dob = args["dob"], email = args["email"])
            counselbook_json = counselbook.json()
            db.session.add(counselbook)
            db.session.commit()
            subject = f"{counselbook.fullname} you just made a booking, booking ID;"
            html = f"{counselbook.fullname} made a booking with booking number"
            send_email(sup_email,subject,html)
            return {
                "status": 200,
                "message": "Booking successful",
                "user"   : counselbook_json
                },200
        return {"status": "BAD REQUEST"},404
    