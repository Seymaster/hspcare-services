""" init.py """
from flask import Flask,jsonify
from mongoengine import connect
from flask_restful import Api
from flask_cors import CORS






""" Application settings"""
app = Flask(__name__,instance_relative_config=True)
api = Api(app)





""" Database and migration mini settings"""
app.config.from_object('config')
app.config.from_pyfile('config.py')
connect(host = app.config['MONGOURI'])


# To allow cross-origin 
cors = CORS(app)
# Endpoints
from Services.forlog.views import Foreignlogapi
from Services.contactus.views import Contactusapi
api.add_resource(Foreignlogapi, '/api/v1/forlog')
api.add_resource(Contactusapi,'/api/v1/contact-us')