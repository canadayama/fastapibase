from fastapi import status
from unittest import TestCase
from ...tests import client

def test_root():
    """"""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    TestCase().assertDictEqual({'server': 'alive', 'name': 'John Smith'},response.json())
    print(response.json())
