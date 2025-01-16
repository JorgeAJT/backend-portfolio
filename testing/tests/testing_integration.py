from fastapi.testclient import TestClient
from testing.src import router

test_client = TestClient(router, "http://127.0.0.1:8080")


def test_say_hello():
    response = test_client.get("/hello/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello Jorge"}