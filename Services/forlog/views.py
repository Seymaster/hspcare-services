from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Foreignlog,json
from Services.medlog.mail import send_email
from instance.setins import sup_email
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
        if all([args.get(field, False) for field in ["fullname","dob","email"]]):
            foreignbook = Foreignlog(fullname = args["fullname"], dob = args["dob"], email = args["email"])
            foreignbook_json = foreignbook.json()
            db.session.add(foreignbook)
            db.session.commit()
            subject = f"{foreignbook.fullname} you just made a booking, booking ID;"
            html = f"{foreignbook.fullname} made a booking with booking number"
            send_email(sup_email,subject,html)
            return {
                "status": 200,
                "message": "Booking successful",
                "user"   : foreignbook_json
                },200
        return {"status": "BAD REQUEST"},404
