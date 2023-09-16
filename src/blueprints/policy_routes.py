from flask import Blueprint, jsonify, request
from database.db_conn import create_session
from models.db_models import Policy, Base
import random
import string

policy_routes = Blueprint("policy_routes", __name__)


@policy_routes.route("/create_policy", methods=["POST"])
def create_policy():
    try:
        json_payload = request.get_json()
    
        Session, engine = create_session()  # Create a session and engine

        # Create a new session for this operation
        with Session() as session:
            policy = Policy(sid=json_payload["sid"], effect=json_payload["effect"], statements=json_payload["statements"], owner=json_payload["statements"],)
            session.add(policy)
            session.commit()

        return jsonify({"message": "New policy created successfully"})
    except Exception as e:
        return jsonify({"error": f"Failed to create new policy: {str(e)}"}), 500
    

@policy_routes.route("/list_policies", methods=["GET"])
def list_policies():
    try:
        Session, engine = create_session()  # Create a session and engine

        # Create a new session for this operation
        with Session() as session:
            users = session.query(Policy).all()

        return jsonify(users)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch user list: {str(e)}"}), 500
    

@policy_routes.route("/drop_policies_table", methods=["get"])
def drop_policies_table():
    try:
        Session, engine = create_session()  # Create a session and engine

        # Create a new session for this operation
        Policy.__table__.drop(engine)

        return jsonify({"message": "policies table successfully"})
    except Exception as e:
        return jsonify({"error": f"Failed to drop policies table: {str(e)}"}), 500
