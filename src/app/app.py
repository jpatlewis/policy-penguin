from flask import Flask, jsonify
from database.db_conn import create_session  # Import the create_session function
from database.db_models import User  # Import your SQLAlchemy model(s)
import random
import string

app = Flask(__name__)

# Create the SQLAlchemy engine and session factory
engine, Session = create_session()


@app.route('/')
def index():
    return "Hey!"


@app.route('/users')
def list_users():
    # Create a new session
    session = Session()

    try:
        # Use the session to interact with the database
        # Example: Query all users
        users = session.query(User).all()

        # Commit the transaction (if changes were made)
        session.commit()

        for user in users:
            print(user.email)

        return "look at logs dingus"

    except Exception as e:
        # Handle exceptions or roll back changes if an error occurs
        session.rollback()
        # You may want to log the error or handle it in some way

    finally:
        # Close the session
        session.close()


@app.route('/create_test_user', methods=['GET'])
def create_test_user():
    # Generate a unique usernam
    username = generate_unique_username()

    session = Session()

    try:
        # Create a new test user with a unique username
        test_user = User(username=username, email=f"{username}@example.com")

        # Add the test user to the session and commit to the database
        session.add(test_user)
        session.commit()

        # Return a JSON response indicating success
        response = {
            'message': 'Test user created successfully',
            'user_id': test_user.id,
            'username': test_user.username,
            'email': test_user.email
        }

        return jsonify(response), 201

    except Exception as e:
        session.rollback()
        return jsonify({'error': 'Failed to create test user'}), 500

    finally:
        session.close()


def generate_unique_username(length=8):
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return username