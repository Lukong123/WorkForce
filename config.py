import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-work-pays'
    SQLAlCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLACHEMY_TRACK_MODIFICATIONS = False


