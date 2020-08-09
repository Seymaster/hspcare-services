import mongoengine as medb
import json
from datetime import datetime

class Foreignlog(medb.Document):
    userId        = medb.StringField(required=True, max_length=100,unique=True)
    treatmentType = medb.StringField(required=True)
    country       = medb.StringField(required=True, max_length=40)
    pda           = medb.StringField(required=True)
    createdAt     = medb.DateTimeField(default=datetime.utcnow)


    def json(self):
        return {'treatmentType': self.treatmentType, 'country': self.country, 'pda': self.pda}



class Contactus(medb.Document):
    firstname = medb.StringField(required=True,max_length=50)
    lastname  = medb.StringField(required=True,max_length=50)
    email     = medb.EmailField(required=True,max_length=50)
    message   = medb.StringField(required=True,max_length=500,unique = True)
    createdAt = medb.DateTimeField(default=datetime.utcnow)


    def json(self):
        return {'firstname': self.firstname,'lastname': self.lastname, 'email': self.email, 'message': self.message}
