from flask import Blueprint, jsonify, request
from database.db_conn import create_session
from models.db_models import Policy
import random
import string

Policy.__table__.drop()