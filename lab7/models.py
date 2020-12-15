"""model for the database"""
from flask_login import UserMixin
from . import db


class User(UserMixin, db.Model):
    """user db model for the table with data storing information"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
