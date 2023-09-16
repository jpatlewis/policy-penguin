from flask import Flask
from models.db_models import User
from models.db_models import Policy
from models.model_manager import ModelManager
from database.db_conn import create_session
from database.build_tables import init_db
import random
import string
import openai

def create_app():
    app = Flask(__name__)

    # Register the user_routes Blueprint
    from blueprints.user_routes import user_routes
    from blueprints.policy_routes import policy_routes
    
    app.register_blueprint(user_routes)
    app.register_blueprint(policy_routes)

    @app.route("/")
    def index():
        return "Hey!!!!"
    
    @app.route("/build_table")
    def build_build():
        init_db(Policy)
        return "hopefully that worked"


    # Other routes and application logic here

    return app
