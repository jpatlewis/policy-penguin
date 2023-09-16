from flask import Flask
from models.db_models import User
from models.model_manager import ModelManager
from database.db_conn import create_session
import random
import string
import openai

def create_app():
    app = Flask(__name__)

    # Register the user_routes Blueprint
    from blueprints.user_routes import user_routes
    app.register_blueprint(user_routes)

    @app.route('/')
    def index():
        return "Hey!!!!"

    # Other routes and application logic here

    return app
