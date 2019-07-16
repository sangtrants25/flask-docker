from flask import Flask, jsonify
from flask_restful import Resource, Api
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

# from flask_superadmin import Admin

import os
import click

db = SQLAlchemy()
admin = Admin()

@click.command()
@with_appcontext
def create_db():

    db.drop_all()
    db.create_all()
    db.session.commit()

@click.command()
@with_appcontext
def seed_db():
    """Seeds the database."""
    from app.models import User
    db.session.add(User(username='sangtrants', email="sangtrants@gmail.com"))

    db.session.commit()


def create_app(script_info=None):
    static = (os.path.dirname(os.path.abspath(__file__)))
    # static = os.path.abspath(os.path.join(static, os.pardir))
    static = os.path.join(static, 'static')

    print(static)
    app = Flask(__name__, static_folder=static)
    app.config.from_object(config[os.getenv('APP_SETTINGS')])

    db.init_app(app)
    admin.init_app(app)

    from app.api import users_blueprint
    from app.main import main_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(main_blueprint)
    
    # add cli command
    app.cli.add_command(create_db)
    app.cli.add_command(seed_db)

    from .models import User
    from .admin_models import UserView
    admin.add_view(UserView(User, db.session))

    @app.shell_context_processor
    def ctx():
        return { 'app': app, 'db':db }
    return app

