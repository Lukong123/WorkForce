from datetime import datetime
from enum import unique
from app import db



class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Company(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    companynumber = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Company {}>'.format(self.companyname)
"""
class Sector(db.Model):
    sector_id = db.Column(db.Integer, primary_key=True)
    sectorname = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    company_id = db.Column(db.Integer, db.ForeignKey('company.id'))

    def __repr__(self):
        return '<Sector {}>'.format(self.sectorname)

class Jobs(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'))

    def __repr__(self):
        return '<Jobs {}>'.format(self.job_name)

"""