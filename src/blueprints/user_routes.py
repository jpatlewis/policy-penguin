from flask import Blueprint, jsonify, request
from database.db_conn import create_session
from models.db_models import User
import random
import string

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/create_user", methods=["GET"])
def create_user():
    try:
        new_username = request.args.get("username")
        new_email = request.args.get("email")

        Session, engine = create_session()  # Create a session and engine

        # Create a new session for this operation
        with Session() as session:
            user = User(username=new_username, email=new_email)
            session.add(user)
            session.commit()

        return jsonify({"message": "New user created successfully"})
    except Exception as e:
        return jsonify({"error": f"Failed to create new user: {str(e)}"}), 500


@user_routes.route("/generate_random_user", methods=["GET"])
def generate_random_user():
    try:
        username = generate_unique_username()

        Session, engine = create_session()  # Create a session and engine

        # Create a new session for this operation
        with Session() as session:
            user = User(username=username, email=f"{username}@example.com")
            session.add(user)
            session.commit()

        return jsonify({"message": "Random user created successfully"})
    except Exception as e:
        return jsonify({"error": f"Failed to create random user: {str(e)}"}), 500


@user_routes.route("/list_users", methods=["GET"])
def list_users():
    try:
        Session, engine = create_session()  # Create a session and engine

        # Create a new session for this operation
        with Session() as session:
            users = session.query(User).all()
            user_list = [{"username": user.username, "email": user.email} for user in users]

        return jsonify(user_list)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch user list: {str(e)}"}), 500


def generate_unique_username(length=8):
    username = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    return username
