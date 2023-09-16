from sqlalchemy import Column, Integer, String, ARRAY, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)


class Policy(Base):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    effect = Column(String)
    statements = Column(ARRAY(JSON))
    owner = Column(String)

    # def add_statement(self, effect, actions, resources, conditions=None):
    #     statement = {
    #         "Effect": effect,
    #         "Action": actions if isinstance(actions, list) else [actions],
    #         "Resource": resources if isinstance(resources, list) else [resources],
    #     }

    #     if conditions:
    #         statement["Condition"] = conditions
    #         self.statements.append(statement)
    #         return Policy


# Other models can be defined here
