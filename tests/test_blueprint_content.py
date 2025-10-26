"""This is a test script to test flask application"""
import pytest
from wsgi import app



@pytest.fixture(name="client")
def create_client():
    """initialize a fixture test client for flask unit testing"""
    with app.test_client() as app_client:
        yield app_client

def test_main_page_content(client):
    """flask unit testing for content in default page"""


def test_about_page_content(client):
    """flask unit testing for content in about page"""

