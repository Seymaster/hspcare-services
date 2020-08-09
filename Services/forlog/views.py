""" views.py , its receives user input and send a email to the 
    application support email that a user just made a booking 
"""

from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services import db
from Services.models import Foreignlog,json
from Services.forlog.mail import send_mail
from instance.setins import sup_email
from sqlalchemy.exc import IntegrityError,OperationalError,InternalError
import json



# middleware
parser = reqparse.RequestParser()


class Foreignlogapi(Resource):
    
    def post(self):
        parser.add_argument("userId",        location='headers',type=int,required=True)
        parser.add_argument("treatmentType", type=str,required=True)
        parser.add_argument("country",       type=str,required=True)
        parser.add_argument("preferredDate", type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["treatmentType","country","preferredDate"]]):
            foreignbook = Foreignlog(userId = args["userId"],treatmentType= args["treatmentType"], country = args["country"], pda = args["preferredDate"])
            foreignbook_json = foreignbook.json()
            try:
                db.session.add(foreignbook)
                db.session.commit()
                send_mail(recipient=sup_email)
                return {"status": 200,
                    "message": "Booking successful",
                    "user"   : foreignbook_json
                    },200
            except IntegrityError:
                db.session.rollback()
                return {
                    "status": 200,
                    "message": "Order already exists"
                },400
        return {"status": "BAD REQUEST"},404
