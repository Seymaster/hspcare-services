from flask import request,jsonify,Response
from flask_restful import Resource,reqparse
from Services.contactus.mail import send_mail
from instance.setins import sup_email
from Services.models import Contactus,json
from sqlalchemy.exc import IntegrityError,OperationalError,InternalError
import json

# middleware 
parser = reqparse.RequestParser()

class Contactusapi(Resource):
    def get(self):
        contactus = Contactus.objects()
        data = [contactus.json() for contact in contactus]
        # print(data)
        return jsonify({
                "status" :200,
                "message": "Fetched All contact-us",
                "data" :  {"data": data}
            }),200

    def post(self):
        parser.add_argument("firstname",type=str,required=True)
        parser.add_argument("lastname", type=str,required=True)
        parser.add_argument("email",    type=str,required=True)
        parser.add_argument("message",  type=str,required=True)
        args = parser.parse_args()
        if all([args.get(field, False) for field in ["firstname","lastname","email","message"]]):
            contactus = Contactus(firstname= args["firstname"], lastname= args["lastname"],email= args["email"], message= args["message"])
            contactus_json = contactus.json()
            try:
                contactus.save()
                send_mail(contactus.firstname,recipient=sup_email)
                return {
                    "status": 200,
                    "message": "Message sent successful",
                    "user"   : contactus_json
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