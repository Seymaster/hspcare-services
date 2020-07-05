""" views.py , its receives user input and send a email to the 
    application support email that a user just made a booking 
"""

from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Longtermcare,json
from Services.medlog.mail import send_mail
from instance.setins import sup_email
from sqlalchemy.exc import IntegrityError,OperationalError,InternalError
import requests
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
            try:
                db.session.add(longtermbook)
                db.session.commit()
                send_mail(longtermbook.fullname,recipient=sup_email)
                return {
                    "status": 200,
                    "message": "Booking successful",
                    "user"   : longtermbook_json
                    },200
            except IntegrityError:
                db.session.rollback()
                return {
                    "status": 200,
                    "message": "User already exists"
                },400
        return {"status": "BAD REQUEST"},404