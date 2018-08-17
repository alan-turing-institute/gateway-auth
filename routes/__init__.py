"""
Routes module
"""

from .auth_routes import RegisterApi, LoginApi, UserApi, LogoutApi
from .fake_routes import TestData


def setup_routes(app, api):
    """
    Set up the routes for these api end points
    """

    api.add_resource(RegisterApi, "/auth/register")
    api.add_resource(LoginApi, "/auth/login")
    api.add_resource(UserApi, "/auth/status")
    api.add_resource(LogoutApi, "/auth/logout")

    # Only while in development
    api.add_resource(TestData, "/test")
