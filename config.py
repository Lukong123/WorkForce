"""
This file is used to store configuration variables 
rather than putting the configuration the same place where the app is created
"""

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-work-pays'