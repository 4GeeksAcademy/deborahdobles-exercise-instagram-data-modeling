import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(50), nullable=False)
    first_name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column(String(80), nullable=False)
    password = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))

class Post(Base):
     __tablename__ = 'post'
     id = Column(Integer, primary_key=True)
     url = Column (String(250), nullable=False)
     user_id = Column(Integer, ForeignKey('user.id'))
     location = Column(String(100))
     description = Column (String(250))
     likes = Column(Integer)
     comments = Column (String(250))

class Media(Base):
     __tablename__ = 'media'
     id = Column(Integer, primary_key=True)
     post_id=Column(ForeignKey('post.id'))

class Favorite(Base):
    __tablename__ = 'Favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_img = Column(Integer, ForeignKey('post.id'))   

class Commment (Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))   
    author_id = Column(Integer, ForeignKey('user.id'))

def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e