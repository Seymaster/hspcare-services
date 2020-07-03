import os
import datetime
from instance.setins import sqlusername,sqlpassword

DEBUG = True

# Globally database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://oluwaseyi:English2018@db4free.net:3306/hspbooking1'
SQLACHEMY_TRACK_MODIFICATIONS = True


# Mail configurations
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True 
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = "squadbytevoluteers@gmail.com"
MAIL_USERNAME = "squadbytevoluteers@gmail.com"
MAIL_PASSWORD = "English2018"


