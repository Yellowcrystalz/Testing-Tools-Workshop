import pytest
from fastapi.testclient import TestClient
import httpx
from calc_api import app

client = TestClient(app)

@pytest.mark.parametrize("a, b, result", [
    (10, 5, 15),
    (5, 10, 15),
    (10, -5, 5)
])
def test_add(a, b, result):
    response = client.get("/add/", params={"a": a, "b": b})
    assert response.json() == {"sum": result}

def test_subtract():
    response = client.get("/subtract/", params={"a": 10, "b": 5})
    assert response.json() == {"difference": 5}

def test_multiply():
    response = client.get("/multiply/", params={"a": 10, "b": 5})
    assert response.json() == {"product": 50}

def test_divide():
    response = client.get("/divide/", params={"a": 10, "b": 5})
    assert response.json() == {"quotient": 2}

def test_divide_by_zero():
    response = client.get("/divide/", params={"a": 10, "b": 0})
    assert response.status_code == 400
    err_msg = response.json()["detail"]
    assert err_msg == "Cannot divide by zero"