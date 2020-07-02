""" views.py , its receives user input and send a email to the 
            application support email that a user just made a booking """

from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Bookings,json
from Services.medlog.mail import send_email
from instance.config import sup_email
from Services.medlog.bookid import generate_random_number
from sqlalchemy.exc import IntegrityError
import json


# middleware
parser = reqparse.RequestParser()


class Medlogapi(Resource):
    def get(self):
        return "Landing page"


    def post(self):
        parser.add_argument("fullname", type=str ,required=True)
        parser.add_argument("dob", type=int,required=True)
        parser.add_argument("phone", type=int,required=True)
        parser.add_argument("address", type=str,required=True)
        parser.add_argument("email", type=str,required=True)
        parser.add_argument("marital", type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["fullname", "dob","phone","address","email","marital"]]):
            book = Bookings(fullname = args["fullname"], dob = args["dob"], phone = args["phone"],
                         address = args["address"],email = args["email"],marital = args["marital"])
            book_json = book.json()
            try:
                db.session.add(book)
                db.session.commit()
                bookid = generate_random_number()
                subject = f"{book.fullname} you just made a booking, booking ID; {bookid}"
                html = f"{book.fullname} Your order for booking with booking number {bookid} has been received"
                send_email(sup_email,subject,html)
                return {
                    "status": 200,
                    "message": "Booking successful",
                    "user"   : book_json
                    },200
        return {"status": "BAD REQUEST"},404
                    
