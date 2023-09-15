import json

class User:
    def __init__(self, username, description=None, email=None):
        
        __tablename__ = "users"
        self.name = username
        self.description = description
        self.email = email

class IamPolicy:
    def __init__(self, name, description=None):

        __tablename__ = 'policies'
        self.name = name
        self.description = description
        self.statements = []

    def add_statement(self, effect, actions, resources, conditions=None):
        statement = {
            "Effect": effect,
            "Action": actions if isinstance(actions, list) else [actions],
            "Resource": resources if isinstance(resources, list) else [resources],
        }
        if conditions:
            statement["Condition"] = conditions
        self.statements.append(statement)

    def to_json(self):
        policy_dict = {
            "Version": "2012-10-17",
            "Statement": self.statements,
        }
        if self.description:
            policy_dict["Description"] = self.description
        return json.dumps(policy_dict, indent=2)