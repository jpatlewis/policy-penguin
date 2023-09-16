import unittest
import random
import string
from sqlalchemy.orm import sessionmaker
from models.definitions.user import User
from models.model_manager import ModelManager
from database.db_conn import create_session


def generate_unique_username(length=8):
    """Generate a unique username."""
    # Define the character set to use for the username (you can customize this)
    characters = string.ascii_letters + string.digits

    # Generate a random username of the specified length
    username = ''.join(random.choice(characters) for _ in range(length))

    return username


class TestDatabaseOperations(unittest.TestCase):
    def setUp(self):
        # Set up the testing environment
        engine, Session = create_session()
        self.session = Session()

    def tearDown(self):
        # Clean up after each test
        self.session.close()

    def test_create_user(self):
        # Test creating a user and querying it from the database
        # Generate a unique username (e.g., using a function)
        username = generate_unique_username()
        email = f"{username}@pp.com"

        # Create a User object
        user = User(username=username, email=email)

        # Create the user in the database
        user_manager = ModelManager(User, self.session)
        user_manager.create(user)

        # Query the user from the database
        queried_user = user_manager.read(user.id)

        # Assert that the queried user matches the created user
        self.assertEqual(user.username, queried_user.username)
        self.assertEqual(user.email, queried_user.email)
