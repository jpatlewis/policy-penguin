from database.db_conn import create_session
from models.db_models import Policy, Base

Session, engine = create_session()


def init_db(model):

    model.__table__.create(engine)