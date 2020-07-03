""" init.py """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_mail import Mail
import datetime





""" Application settings"""
app = Flask(__name__,instance_relative_config=True)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'squadbytevoluteers@gmail.com',
    MAIL_PASSWORD = 'English2018',
    MAIL_DEFAULT_SENDER = 'squadbytevoluteers@gmail.com'
))

api = Api(app)



"""   Flask Mail Settings """
mail = Mail(app)



""" Database and migration mini settings"""
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app,db)





# Endpoints
from Services.medlog.views import Medlogapi
from Services.forlog.views import Foreignlogapi
from Services.longtermcare.views import Longtermlogapi
from Services.counselling.views import Counselapi
api.add_resource(Medlogapi, '/medical-logistics/make-booking')
api.add_resource(Foreignlogapi, '/foreign-logistics/make-booking')
api.add_resource(Longtermlogapi, '/long-term-support/make-booking')
api.add_resource(Counselapi, '/counselling/make-booking')