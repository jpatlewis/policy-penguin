from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import database.db_conn as db_conn
from database.db_models import User, Policy

# Create a new user
new_user = User(username='joe_schmoe', email='joe@example.com')
session = db_conn.Session()
session.add(new_user)
session.commit()

# Query the database
user = session.query(User).filter_by(username='joe_schmoe').first()
print(user.username, user.email)

# Close the session
session.close()
