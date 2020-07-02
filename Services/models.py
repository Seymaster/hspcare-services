from Services import db
from Services import Migrate
import json
from datetime import datetime


class Bookings(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    fullname      = db.Column(db.String(128))
    dob           = db.Column(db.Integer)
    phone         = db.Column(db.Integer,unique=True)
    address       = db.Column(db.String(200),nullable=False)
    email         = db.Column(db.String(64), unique=True, index=True)
    marital       = db.Column(db.String(64),nullable=False)
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,phone,address,email,marital):
        self.fullname = fullname
        self.dob = dob
        self.phone = phone
        self.address = address
        self.email    = email
        self.marital = marital

    def json(self):
        return {'fullname': self.fullname, 'dob': self.dob, 'phone': self.phone, 'address': self.address,
            'email': self.email,'marital': self.marital}


class Foreignlog(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    fullname      = db.Column(db.String(120))
    dob           = db.Column(db.Integer)
    email         = db.Column(db.String(64), unique=True, index=True)
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,email):
        self.fullname = fullname
        self.dob = dob
        self.email = email

    def json(self):
        return {'fullname': self.fullname, 'dob': self.dob, 'email': self.email}



class Longtermcare(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    fullname      = db.Column(db.String(120))
    dob           = db.Column(db.Integer)
    email         = db.Column(db.String(64), unique=True, index=True)
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,email):
        self.fullname = fullname
        self.dob = dob
        self.email = email

    def json(self):
        return {'fullname': self.fullname, 'dob': self.dob, 'email': self.email}


class Counselling(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    fullname      = db.Column(db.String(120))
    dob           = db.Column(db.Integer)
    email         = db.Column(db.String(64), unique=True, index=True)
    date          = db.Column(db.DateTime,nullable=True,default=datetime.now())

    def __init__(self,fullname,dob,email):
        self.fullname = fullname
        self.dob = dob
        self.email = email

    def json(self):
        return {'fullname': self.fullname, 'dob': self.dob, 'email': self.email}    




db.create_all()