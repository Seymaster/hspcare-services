""" views.py , its receives user input and send a email to the 
    application support email that a user just made a booking 
"""

from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Counselling,json
from Services.medlog.mail import send_mail
from instance.setins import sup_email
from sqlalchemy.exc import IntegrityError,OperationalError,InternalError
import requests
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
            try:
                db.session.add(counselbook)
                db.session.commit()
                send_mail(counselbook.fullname,recipient=sup_email)
                return {
                    "status": 200,
                    "message": "Booking successful",
                    "user"   : counselbook_json
                    },200
            except IntegrityError:
                db.session.rollback()
                return {
                    "status": 200,
                    "message": "User already exists"
                },400
        return {"status": "BAD REQUEST"},404
    