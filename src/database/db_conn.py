from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    DATABASE_URL = "postgresql://myuser:mypassword@db:5432/mydatabase"

    if not DATABASE_URL:
        raise Exception("DATABASE_URL environment variable is not set.")

    # Create the SQLAlchemy engine and session factory
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)

    return engine, Session
