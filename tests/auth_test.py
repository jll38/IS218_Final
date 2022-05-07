from app.db.models import User
from app.auth.forms import register_form
from app.auth import register
"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_register(client):
    form = register_form
    form.email.data = "test@testmail.com"
    form.password.data = "password"
    register()
