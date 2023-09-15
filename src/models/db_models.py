from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    #id = Column(Integer, primary_key=True) need to figure this out
    name = Column(String)
    description = Column(String)
    email = Column(String)

class Policy(Base):
    __tablename__ = 'policies'

    #id = Column(Integer, primary_key=True) need to figure this out
    name = Column(String)
    description = Column(String)
    email = Column(ARRAY(Json))
