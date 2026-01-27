import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/api/v1/users/", json={"username": "test", "email": "test@example.com", "password": "pass123"})
    assert response.status_code == 200
    assert response.json()["username"] == "test"
