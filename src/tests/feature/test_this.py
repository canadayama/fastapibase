from fastapi import status
from fastapi.testclient import TestClient
from unittest import TestCase
from ...main import app, get_name

def get_my_name():
    """"""
    return "Richard Hayashi"


app.dependency_overrides[get_name] = get_my_name
client = TestClient(app)

def test_root():
    """"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    TestCase().assertDictEqual({'server': 'alive', 'name': 'Richard Hayashi'},response.json())
    print(response.json())
