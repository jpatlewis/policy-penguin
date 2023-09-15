from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace 'postgresql://username:password@localhost/database_name' with your PostgreSQL connection string
db_url = 'postgresql://peng-dev:peng@localhost/penguin'

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)