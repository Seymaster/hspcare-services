import datetime
import os

DEBUG = True

# Globally database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://root@db4free.net:3306/hspbookings'
SQLACHEMY_TRACK_MODIFICATIONS = True


# Mail configurations
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True 
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = "myers12919@gmail.com"
MAIL_USERNAME = 'myers12919@gmail.com'
MAIL_PASSWORD = "EVerything_123"


#  locally database configuration
# SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/service1'
# SQLACHEMY_TRACK_MODIFICATIONS = False

# Support email
sup_email = "alugbinoluwaseyi1@gmail.com"