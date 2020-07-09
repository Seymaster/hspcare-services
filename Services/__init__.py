""" init.py """

from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS






""" Application settings"""
app = Flask(__name__,instance_relative_config=True)
api = Api(app)





""" Database and migration mini settings"""
app.config.from_object('config')
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Migrate(app,db)

# To allow cross-origin 
cors = CORS(app)

# Error handling
# def networkerror():
#     if OperationalError:
#         return jsonify({
#             "status": 500,
#             "message": "Check your internet"
#         })
# networkerror()

# Endpoints
from Services.medlog.views import Medlogapi
from Services.forlog.views import Foreignlogapi
from Services.longtermcare.views import Longtermlogapi
from Services.counselling.views import Counselapi
api.add_resource(Medlogapi, '/api/medlog/make-booking')
api.add_resource(Foreignlogapi, '/api/forlog/make-booking')
api.add_resource(Longtermlogapi, '/api/longtermcare/make-booking')
api.add_resource(Counselapi, '/api/counselling/make-booking')