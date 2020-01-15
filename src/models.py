import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class Profile(Base) :
    __tablename__='profile' 
    user_name = Column(String(250),primary_key=True)
    name = Column(String(250))
    gender = Column(String(100))
    email = Column(String(250))
    phone_no =Column(Integer)

class Subscribeto(Base):
    __tablename__='subscribeto' 
    user_name = Column(String(250), primary_key=True)
    feedback = Column(Boolean)
    news = Column(Boolean)
    reminder = Column(Boolean)
    product = Column(Boolean)
    shopping_bag = Column(Boolean)
    profile_user_name = Column(String(250),ForeignKey('profile.user_name'))
    profile = relationship(Profile)

class Loginactivity(Base):
    __tablename__='loginactivity' 
    user_name = Column(String(250), primary_key=True)
    addrtess = Column(String(250))
    status = Column(String(250))
    login_time = Column(Integer)
    profile_user_name = Column(String(250),ForeignKey('profile.user_name'))    
    profile = relationship(Profile)

class Post(Base):
    __tablename__='post' 
    user_name = Column(String(250), primary_key=True)
    post_date_time = Column(Integer) 
    no_of_likes = Column(Integer)
    no_of_commands = Column(Integer)
    bookmark = Column(Integer)
    profile_user_name = Column(String(250),ForeignKey('profile.user_name'))    
    profile = relationship(Profile)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')