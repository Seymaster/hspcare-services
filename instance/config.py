import os
import datetime
from instance.setins import sqlusername,sqlpassword

DEBUG = True

# Globally database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://{0}:{1}@db4free.net:3306/hspbooking1'.format(sqlusername,sqlpassword)
SQLACHEMY_TRACK_MODIFICATIONS = True


