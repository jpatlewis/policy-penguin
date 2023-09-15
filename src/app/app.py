from flask import Flask, render_template
from database.db_conn import create_session  # Import the create_session function
from database.db_models import User  # Import your SQLAlchemy model(s)

app = Flask(__name__)

# Create the SQLAlchemy engine and session factory
engine, Session = create_session()

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/users')
def list_users():
    # Create a new session
    session = Session()

    try:
        # Use the session to interact with the database
        # Example: Query all users
        users = session.query(User).all()

        # You can perform other database operations here

        # Commit the transaction (if changes were made) and close the session
        session.commit()
    except Exception as e:
        # Handle exceptions or roll back changes if an error occurs
        session.rollback()
        # You may want to log the error or handle it in some way

    finally:
        # Close the session
        session.close()

    # Render a template with the retrieved data
    return render_template('users.html', users=users)

