from app import create_app

def test_homepage(client):
    """index page test"""
    response = client.get("/")
    assert response.status_code == 200

def test_register_page(client):
    """register page test"""
    response = client.get("/register")
    assert response.status_code == 200

def test_login_page(client):
    """login page test"""
    response = client.get("/login")
    assert response.status_code == 200