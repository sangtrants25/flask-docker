from flask import Flask, jsonify
from flask_restful import Resource, Api
from config import config
from flask_sqlalchemy import SQLAlchemy
from flask.cli import with_appcontext

import os
import click

db = SQLAlchemy()

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
    from app.api.models import User
    db.session.add(User(username='michael', email="hermanmu@gmail.com"))
    db.session.add(User(username='michaelherman', email="michael@mherman.org"))
    db.session.commit()


def create_app(script_info=None):
    app = Flask(__name__)
    app.config.from_object(config[os.getenv('APP_SETTINGS')])
    db.init_app(app)

    from app.api import users_blueprint
    app.register_blueprint(users_blueprint)
    
    # add cli command
    app.cli.add_command(create_db)
    app.cli.add_command(seed_db)

    @app.shell_context_processor
    def ctx():
        return { 'app': app, 'db':db }
    return app

