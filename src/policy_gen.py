import json
from models.models import IamPolicy

# Create an IAM policy instance
my_policy = IamPolicy("MyPolicy", "Description of My IAM Policy")

# Add statements to the policy
my_policy.add_statement("Allow", "s3:ListBucket", "arn:aws:s3:::example-bucket")
my_policy.add_statement("Allow", ["s3:GetObject", "s3:PutObject"], "arn:aws:s3:::example-bucket/*")

# Convert the policy to JSON format
policy_json = my_policy.to_json()

# Print the JSON representation of the policy
print(policy_json)


