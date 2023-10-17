from fastapi.testclient import TestClient
from ..main import app, get_name
from ..config import Settings

def get_my_name():
    """"""
    return "John Smith"

app.dependency_overrides[get_name] = get_my_name
client = TestClient(app)

print(Settings().model_dump())