from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import database.db_conn as db_conn

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)

# Create tables
Base.metadata.create_all(db_conn.engine)

# Create a new user
new_user = User(username='john_doe', email='john@example.com')
session = db_conn.Session()
session.add(new_user)
session.commit()

# Query the database
user = session.query(User).filter_by(username='john_doe').first()
print(user.username, user.email)

# Close the session
session.close()
