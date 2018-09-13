import json
import jwt

from .decorators import request_context
from .fixtures import demo_app

from routes import RegisterApi, LoginApi
from connection.models import User


@request_context(
    "/auth/register",
    data='{"username": "turing", "password": "turing"}',
    content_type="application/json",
    method="POST",
)
def test_register(demo_app):
    """
    Test that we can register a user
    """

    # register a new user
    result = RegisterApi().dispatch_request()
    assert result.status_code == 201

    # convert to dict for inspection
    data = json.loads(result.data)
    assert data["status"] == "success"

    # check that the username is stored in the database
    user = User.query.filter(User.username == "turing").first()
    assert user.username == "turing"


@request_context(
    "/auth/login",
    data='{"username": "turing", "password": "turing"}',
    content_type="application/json",
    method="POST",
)
def test_login(demo_app):
    """
    Test that we can log in
    """

    # register a new user
    result = LoginApi().dispatch_request()
    assert result.status_code == 200

    # convert to dict for inspection
    data = json.loads(result.data)
    assert data["status"] == "success"

    # check that the username is stored in the database
    auth_token = data["auth_token"]
    key = demo_app.config.get("SECRET_KEY")
    payload = jwt.decode(auth_token, key)

    # check that the username is stored in the jwt token
    assert payload["name"] == "turing"

