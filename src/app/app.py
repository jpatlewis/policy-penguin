from flask import Flask, jsonify
from database.db_conn import create_session
from database.db_models import User
# from request_factory.request_factory import ApiRequestFactory
from config.config import GPT_API_KEY
import random
import string
import openai

app = Flask(__name__)
# This key isn't valid because you didn't pay for a key
openai.api_key = GPT_API_KEY

# Create the SQLAlchemy engine and session factory
engine, Session = create_session()


@app.route('/')
def index():
    return "Hey!!!!"


@app.route('/req')
def req():
    status_message = "things are weird"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "system",
                "content": "is my key valid?"
            }]
        )

        if response.status_code == 200:
            # Things are good
            print(response.choices[0].text)
            status_message = "things are good"
        else:
            # Things are bad
            print(f"Failed with status code: {response.status_code}")
            status_message = f"Failed with status code: {response.status_code}"

    except openai.OpenAIError as e:
        # Handle OpenAI-specific errors
        print(f"OpenAI API error: {str(e)}")
        status_message = str(e)
    except Exception as e:
        # Other unexpected errors
        print(f"An unexpected error occurred with OpenAI request: {str(e)}")
        status_message = str(e)

    return status_message


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

        return "Look at logs dingus"

    except Exception as e:
        # Handle exceptions or roll back changes if an error occurs
        session.rollback()
        # You may want to log the error or handle it in some way

    finally:
        # Close the session
        session.close()


@app.route('/create_test_user', methods=['GET'])
def create_test_user():
    # Generate a unique username
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
