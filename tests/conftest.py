"""This makes the test configuration setup"""
# pylint: disable=redefined-outer-name

import pytest
from app import create_app, db


@pytest.fixture()
def application():
    """This makes the app"""
    application = create_app()
    application.config.update({
        "TESTING": True,
    })
    yield application

    with application.app_context():
        db.create_all()
        yield application
        db.session.remove()

class authMethods:
    def __init__(self, client):
        self._client = client

    def register(self, email="test@email.com", password="Password"):
        return self._client.post("/register", data={"email": email, "password": password, "confirm": password})

    def login(self, email="test@email.com", password="Password"):
        return self._client.post("/login", data={"email": email, "password": password})

    def logout(self):
        return self._client.get("/logout")

@pytest.fixture
def auth(client):
    return authMethods(client)

@pytest.fixture()
def client(application):
    """This makes the http client"""
    return application.test_client()


@pytest.fixture()
def runner(application):
    """This makes the task runner"""
    return application.test_cli_runner()