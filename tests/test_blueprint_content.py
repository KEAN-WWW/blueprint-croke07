"""Tests for homepage/about content rendered by the Blueprint."""
import pytest
from wsgi import app

@pytest.fixture(name="client")
def create_client():
    """Provide a Flask test client."""
    with app.test_client() as client:
        yield client

def test_main_page_content(client):
    """Home returns 200 and contains the word 'Blueprint'."""
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Blueprint" in resp.data

def test_about_page_content(client):
    """About returns 200 and contains the word 'Blueprint'."""
    resp = client.get("/about")
    assert resp.status_code == 200
    assert b"Blueprint" in resp.data
