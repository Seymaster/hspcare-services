""" views.py , its receives user input and send a email to the 
    application support email that a user just made a booking 
"""

from flask import request,jsonify,Response
from flask_restful import Resource,reqparse,inputs
from Services.models import Foreignlog,json
from Services.forlog.mail import send_mail
from instance.setins import sup_email
from mongoengine.errors import FieldDoesNotExist,ValidationError,NotUniqueError
import json



# middleware
parser = reqparse.RequestParser()


class Foreignlogapi(Resource):
    def get(self):
        foreignlog = Foreignlog.objects()
        data = [foreignlog.json() for forlog in foreignlog]
        # print(data)
        return jsonify({
                "status" :200,
                "message": "Fetched All contact-us",
                "data" :  data
            }),200
    

    def post(self):
        parser.add_argument("userId",        location='headers',type=str,required=True)
        parser.add_argument("treatmentType", type=str,required=True)
        parser.add_argument("country",       type=str,required=True)
        parser.add_argument("preferredDate", type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["treatmentType","country","preferredDate"]]):
            foreignbook = Foreignlog(userId = args["userId"],treatmentType= args["treatmentType"], country = args["country"], pda = args["preferredDate"])
            foreignbook_json = foreignbook.json()
            try:
                foreignbook.save()
                send_mail(recipient=sup_email)
                return {"status": 200,
                    "message": "Booking successful",
                    "user"   : foreignbook_json
                    },200
            except NotUniqueError as e:
                x = str(e)
                y = x.split()
                z = y[13]
                message = f'{z[0:6]} already exist'
                return {
                    "status": 500,
                    "message": message
                },500
        return {"status": "BAD REQUEST"},404

        
