from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Longtermcare,json
from Services.medlog.mail import send_email
from instance.config import sup_email
import json

parser = reqparse.RequestParser()


class Longtermlogapi(Resource):
    def get(self):
        return "Landing page for Longterm logistics"

    def post(self):
        parser.add_argument("fullname", type=str ,required=True)
        parser.add_argument("dob", type=int,required=True)
        parser.add_argument("email", type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["fullname","dob","email"]]):
            longtermbook = Longtermcare(fullname = args["fullname"], dob = args["dob"], email = args["email"])
            longtermbook_json = longtermbook.json()
            db.session.add(longtermbook)
            db.session.commit()
            subject = f"{longtermbook.fullname} you just made a booking, booking ID;"
            html = f"{longtermbook.fullname} made a booking with booking number"
            send_email(sup_email,subject,html)
            return {
                "status": 200,
                "message": "Booking successful",
                "user"   : longtermbook_json
                },200
        return {"status": "BAD REQUEST"},404