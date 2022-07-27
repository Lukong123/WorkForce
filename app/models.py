from datetime import datetime
from enum import unique
from uuid import uuid4
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from app import app


@login.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin,db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # id = str(uuid4)

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    db.create_all()
    db.session.commit()

class Company(UserMixin, db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    companynumber = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def get_id(self):
        return self.user_id

    def __repr__(self):
        return '<User {}>'.format(self.companyname)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    db.create_all()
    db.session.commit()


class Sector(db.Model):
    sector_id = db.Column(db.Integer, primary_key=True)
    sectorname = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    companyname = db.Column(db.Integer, db.ForeignKey('company.comapanyname'))

    
    def __repr__(self):
        return '<Sector {}>'.format(self.sectorname)
    
    db.create_all()
    db.session.commit()

class Jobs(db.Model):
    job_id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sectorname = db.Column(db.Integer, db.ForeignKey('sector.sectorname'))

    
    def __repr__(self):
        return '<Sector {}>'.format(self.sectorname)
    db.create_all()
    db.session.commit()
