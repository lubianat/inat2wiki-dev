import os
import sys
import pytest

# ensure the parent directory (src) is on sys.path so app.py can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
