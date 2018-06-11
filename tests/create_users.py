#!/usr/bin/env python

"""
main function, doing the following:
* create Users in the database
"""

from flask import Flask
from flask_restful import Api

from connection import init_database
from connection.models import db, User


def set_up_test_database():
    """
    Set up a user and add to database
    """

    session = db.session
    user = User(username='turing', password='turing', admin=False)

    done = False
    for _ in User.query.all():
        done = True
    if done:
        print('Data already there!')
        exit()

    session.add(user)
    session.commit()


if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = ('postgres_auth://'
                                             'sg:sg@localhost:8082/sg')

    init_database(app)

    api = Api(app)
    with app.app_context():
        set_up_test_database()
