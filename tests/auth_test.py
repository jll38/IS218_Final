from flask import Flask
from flask_login import FlaskLoginClient
import tests
import pytest
from app import db, create_app
from app.db.models import User
from app.auth.forms import register_form
from app.auth import register
from flask_login import logout_user, login_user
"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_dashboard_deny(client):
    """test dashboard access when not logged in"""
    response = client.get("/dashboard")
    assert response.status_code == 302
def test_dashboard_accept(application, client):
    """test dashboard access when logged in"""
    application.test_client_class = FlaskLoginClient
    user = User.query.get(1)

    assert db.session.query(User).count == 1
    assert user.email == 'johncena@gmail.com'

    with application.test_client_class(user=user) as client:
        response = client.get('/dashboard')
        assert response.status_code == 200

# def test_register(client, auth):
#     """register redirecting to login"""
#     response = auth.register()
#     assert response.headers["Location"] == "/login"


