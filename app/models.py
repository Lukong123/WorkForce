from datetime import datetime
from enum import unique
from turtle import back
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
    id = db.Column(db.Integer, primary_key=True)
    companyname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    companynumber = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    sectors = db.relationship('Sector', backref='company')

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.companyname)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    db.create_all()
    db.session.commit()


class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    company = db.Column(db.Integer, db.ForeignKey('company.id'))

    def get_id(self):
        return self.id


    
    def __repr__(self):
        return '<Sector {}>'.format(self.name)
    
    db.create_all()
    db.session.commit()

job_sector = db.Table('job_sector', 
    db.Column(' job_id', db.Integer, db.ForeignKey('Job.id'), primary_key=True),
    db.Column('sector_id', db.Integer, db.ForeignKey('Sector.id'), primary_key=True)
)

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    sector = db.relationship('Sector', secondary='job_sector')

    
    def __repr__(self):
        return '<Sector {}>'.format(self.sectorname)
    db.create_all()
    db.session.commit()
