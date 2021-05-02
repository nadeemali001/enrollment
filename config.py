import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dhuih3hu3uid3hih392hirb2i3hd23'
    MONGODB_SETTINGS = { 'db': 'UTA_Enrollment' }
