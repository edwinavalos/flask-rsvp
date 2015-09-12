from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from extensions import db


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(12), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Invitee(db.Model):
    __tablename__ = 'invitee'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(200))
    address = Column(String(200))

    def __init__(self, first_name=None, last_name=None, email=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address

    def __repr__(self):
        return "<Invitee {} {}>".format(self.first_name, self.last_name)

def create_all(app=None):
    db.create_all(app=app)
