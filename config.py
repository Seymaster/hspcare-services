import os
import datetime
from instance.setins import dbusername,dbpassword


DEBUG = True


# Globally database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MONGOURI = f'mongodb+srv://{dbusername}:<{dbpassword}>@cluster0.2ip3w.mongodb.net/<hspcare>?retryWrites=true&w=majority'



