"""
This module is reponsible for hashing
of user passwords
"""
from flask_bcrypt import Bcrypt

bc = Bcrypt()


def init_bcrypt(app):
    """
    Initialise bcrypt in the context of the relevant flask app
    """
    bc.init_app(app)
