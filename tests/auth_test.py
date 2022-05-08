from app import db
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
    app = current_app
    with app.app_context():
        user = User.query.first()
        user.authenticated = True
        db.session.add(user)
        db.session.commit()
        login_user(user)
        response = client.get('/dashboard')
        assert response == 200

