from flask import Blueprint
from flask_restful import Api

users_blueprint = Blueprint('users',__name__)
api = Api(users_blueprint)

from . import hello, users
