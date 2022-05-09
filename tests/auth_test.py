import tests
import pytest
from app import db, create_app
from app.db.models import User
from app.auth.forms import register_form
from app.auth import register
from flask_login import logout_user, login_user
from flask import current_app

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

def test_dashboard_accept(client):
    """test dashboard access when logged in"""
    with client:
        client.post('/login', data=dict(email='johncena@gmail.com',password='Password'))
        response = client.get('/dashboard')
        assert response == 200

