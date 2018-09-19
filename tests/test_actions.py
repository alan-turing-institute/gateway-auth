import pytest
import json
import jwt

from .decorators import request_context
from .fixtures import demo_app

from routes import RegisterApi, LoginApi, TokenApi
from connection.models import User

cached_auth_token = None


@request_context(
    "/register",
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


@pytest.mark.dependency(depends=["test_register"])
@request_context(
    "/login",
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
    auth_key = demo_app.config.get("AUTH_KEY")
    payload = jwt.decode(auth_token, auth_key)

    # check that the username is stored in the jwt token
    assert payload["name"] == "turing"

    pytest.auth_token = auth_token  # store token for use in dependent tests


@pytest.mark.dependency(depends=["test_login"])
def test_job_token(demo_app):
    with demo_app.app_context():
        auth = f"Bearer {pytest.auth_token}"
        with demo_app.test_request_context(
            "/token?job_id=6ddc5385-02f8-4ce4-996f-9ee92c0fbb5d",
            method="GET",
            headers={"Authorization": auth},
        ):
            result = TokenApi().dispatch_request()
            assert result.status_code == 200

            data = json.loads(result.data)
            job_token = data["job_token"]

            job_key = demo_app.config.get("JOB_KEY")
            payload = jwt.decode(job_token, job_key)

            # a job token contains a job id
            assert payload["job_id"] == "6ddc5385-02f8-4ce4-996f-9ee92c0fbb5d"

            # a job token contains a username
            assert payload["name"] == "turing"
