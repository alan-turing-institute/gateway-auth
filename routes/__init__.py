"""
Routes module
"""

from .auth_routes import RegisterApi, LoginApi, UserApi, LogoutApi, TokenApi
from .fake_routes import TestData


def set_up_routes(app, api):
    """
    Set up the routes for these api end points
    """

    api.add_resource(RegisterApi, "/register")
    api.add_resource(LoginApi, "/login")
    api.add_resource(UserApi, "/status")
    api.add_resource(TokenApi, "/token")
    api.add_resource(LogoutApi, "/logout")

    # Only while in development
    api.add_resource(TestData, "/test")
