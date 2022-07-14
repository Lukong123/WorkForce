<<<<<<< HEAD
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-work-pays'
    SQLAlCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLACHEMY_TRACK_MODIFICATIONS = False
=======
"""
This file is used to store configuration variables 
rather than putting the configuration the same place where the app is created
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-work-pays'
>>>>>>> fce920aeff5892dd8c31e49866e910d7627fc61b
