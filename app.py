#! /usr/bin/env python3
"""
The main entry point for this flask app
"""

import os
from time import sleep
from json import load

from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy.exc import OperationalError

from connection import init_database, init_bcrypt

from routes import setup_routes


config = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
    "default": "config.DevelopmentConfig"
}


def configure_app(app):
    # load config.py options
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app = Flask(__name__, instance_relative_config=True)

logger = app.logger

configure_app(app)

db_loaded = False
while not db_loaded:
    try:
        db_loaded = True
        init_database(app)
    except OperationalError as e:
        db_loaded = False
        logger.error(e)
        sleep(3)

init_bcrypt(app)

api = Api(app)
CORS(app, resources={r'/*': {'origins': '*'}})

setup_routes(app, api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
