import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register():
    response = client.post("/register", json={
        "username": "alice",
        "password": "123"
    })

    assert response.status_code == 200
    assert response.json()["status"] is True


def test_login():
    # first register
    client.post("/register", json={
        "username": "bob",
        "password": "123"
    })

    response = client.post("/login", json={
        "username": "bob",
        "password": "123"
    })

    assert response.status_code == 200
    assert "token" in response.json()