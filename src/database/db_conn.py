from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def create_session():
    # Replace 'postgresql://username:password@localhost/database_name' with your PostgreSQL connection string
    db_url = 'postgresql://peng-dev:peng@localhost/penguin'

    # Create the SQLAlchemy engine and session factory
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    return engine, Session
