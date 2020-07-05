""" views.py , its receives user input and send a email to the 
    application support email that a user just made a booking 
"""
from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from flask_sqlalchemy import sqlalchemy
from Services import db
from Services.models import Bookings,json
from Services.medlog.mail import send_mail
from instance.setins import sup_email
from Services.medlog.bookid import generate_random_number
from sqlalchemy.exc import IntegrityError,OperationalError,InternalError
import requests
import json



# middleware
parser = reqparse.RequestParser()


class Medlogapi(Resource):
    
    def post(self):
        parser.add_argument("fullname", type=str ,required=True)
        parser.add_argument("dob", type=int,required=True)
        parser.add_argument("email", type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["fullname","dob","email"]]):
            book = Bookings(fullname = args["fullname"], dob = args["dob"],email = args["email"])
            book_json = book.json()
            try:
                db.session.add(book)
                db.session.commit()
                send_mail(book.fullname,recipient=sup_email)
                return {
                    "status": 201,
                    "message": "Booking successful",
                    "user"   : book_json
                    },200
            except IntegrityError:
                db.session.rollback()
                return {
                    "status": 200,
                    "message": "User already exists"
                },500
            except Exception:
                return {
                    "status": 403,
                    "message": "check your internet"
                },500
        return {"status": "BAD REQUEST"},404
                    
