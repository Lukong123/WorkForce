from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


@login.user_loader
def load_user(id):
    return User.query.get(id)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(64), index=True, unique=True)
    tel = db.Column(db.String(64), index=True, unique=True)
    role = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))
    sector_id = db.relationship('Sector', backref='user')

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Sector(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    description = db.Column(db.String(200), index=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    company_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job = db.relationship('Jobs', secondary='job_sector')

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Sector {}>'.format(self.name)


job_sector = db.Table('job_sector', 
    db.Column(' job_id', db.Integer, db.ForeignKey('jobs.id'), primary_key=True),
    db.Column('sector_id', db.Integer, db.ForeignKey('sector.id'), primary_key=True)
)


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(200), index=True, unique=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def get_id(self):
        return self.id
    
    def __repr__(self):
        return '<Sector {}>'.format(self.sectorname)

db.create_all()