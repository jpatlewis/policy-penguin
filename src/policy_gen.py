import json
import database.db_conn as db_conn
from models.definitions.user import IamPolicy as Policy
from models.db_models import Policy as Db_Policy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an IAM policy instance
my_policy = Policy("MyPolicy", "Description of My IAM Policy")

# Add statements to the policy
my_policy.add_statement("Allow", "s3:ListBucket", "arn:aws:s3:::example-bucket")
my_policy.add_statement("Allow", ["s3:GetObject", "s3:PutObject"], "arn:aws:s3:::example-bucket/*")

# Convert the policy to JSON format

# Print the JSON representation of the policy
print(my_policy)

#map model to db model
#this is a shitty experience and could be improved
my_policy_db = Db_Policy(name=my_policy.name, description=my_policy.description, statements=my_policy.statements)

# Create a new policy
session = db_conn.Session()
session.add(my_policy_db)
session.commit()

# Query the database
policy = session.query(Db_Policy).filter_by(name=my_policy.name).first()
print(policy.statements)

# Close the session
session.close()
