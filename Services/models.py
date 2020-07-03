from Services import db
from Services import Migrate
import json
from datetime import datetime


class Bookings(db.Model):
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