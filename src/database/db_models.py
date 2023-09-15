from database.db_conn import create_session
from sqlalchemy import Column, Integer, String, ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base

engine, Session = create_session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

class Policy(Base):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    statements = Column(ARRAY(JSON))

Base.metadata.create_all(engine)