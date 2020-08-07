from Services import db
from Services import Migrate
import json
from datetime import datetime

class Foreignlog(db.Model):
    id               = db.Column(db.Integer, primary_key=True)
    treatmenttype    = db.Column(db.String(120))
    country          = db.Column(db.Integer)
    pda              = db.Column(db.String(64), unique=True, index=True)
    date             = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,email):
        self.fullname = fullname
        self.dob = dob
        self.email = email

    def json(self):
        return {'fullname': self.fullname, 'dob': self.dob, 'email': self.email}



class Contactus(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    firstname     = db.Column(db.String(25))
    lastname      = db.Column(db.String(25))
    email         = db.Column(db.String(64), unique=True, index=True)
    message       = db.Column(db.String(250))
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,email):
        self.firstname = firstname
        self.lastname  = lastname
        self.email     = email
        self.message   = message

    def json(self):
        return {'firstname': self.firstname,'lastname': self.lastname, 'email': self.email, 'message': self.message}






db.create_all()