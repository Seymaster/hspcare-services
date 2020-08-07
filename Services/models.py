from Services import db
from Services import Migrate
import json
from datetime import datetime

class Foreignlog(db.Model):
    id               = db.Column(db.Integer, primary_key=True)
    treatmentType    = db.Column(db.String(120))
    country          = db.Column(db.Integer)
    pda              = db.Column(db.String(64), index=True)
    date             = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,treatmentType,country,pda):
        self.treatmentType = treatmentType
        self.country       = country
        self.pda           = pda

    def json(self):
        return {'treatmentType': self.treatmentType, 'country': self.country, 'pda': self.pda}



class Contactus(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    firstname     = db.Column(db.String(25))
    lastname      = db.Column(db.String(25))
    email         = db.Column(db.String(64),index=True)
    message       = db.Column(db.String(500))
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,firstname,lastname,email,message):
        self.firstname = firstname
        self.lastname  = lastname
        self.email     = email
        self.message   = message

    def json(self):
        return {'firstname': self.firstname,'lastname': self.lastname, 'email': self.email, 'message': self.message}






db.create_all()