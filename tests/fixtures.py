# pylint: skip-file
"""
Helpful fixtures for testing
"""
from uuid import uuid4

from flask import Flask
from flask_restful import Api
from pytest import fixture

from connection import init_database, init_bcrypt
from connection.models import db
from routes import set_up_routes


@fixture(scope="module")
def demo_app():
    """
    Setup the flask app context
    """
    app = Flask(__name__)

    app.config.from_json("config.testing.json")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.testing = True

    init_database(app)
    init_bcrypt(app)

    api = Api(app)

    set_up_routes(app, api)

    return app
