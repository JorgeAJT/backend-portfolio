from fastapi.testclient import TestClient
from testing.src import router
from pytest import fixture
import os

@fixture
def environmental_variables():
    os.environ["dbname"] = "postgres"
    os.environ["user"] = "postgres"
    os.environ["password"] = "1234"
    os.environ["host"] = "127.0.0.1"
    os.environ["port"] = "5432"

    return True


@fixture
def test_client():
    return TestClient(router, "http://127.0.0.1:8080")


def test_say_hello(environmental_variables: bool, test_client: TestClient):
    response = test_client.get("/hello/")
    assert response.status_code == 200
    assert response.json() == {"message": "hello Jorge"}


def test_get_names(environmental_variables: bool, test_client: TestClient):
    expected_row = [
        ["Jorge", 34],
        ["David", 25],
        ["Dani", 28],
        ["Paquito", 47]
    ]
    response = test_client.get("/names/")
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {"message": expected_row}


def test_get_mandate_data(environmental_variables: bool, test_client: TestClient):
    expected_row = [
        {
            "mandate_id": 2,
            "business_partner_id": "0101879132",
            "brand": "ES",
            "mandate_status": "Y",
            "collection_frequency": "D",
            "row_update_datetime": "2024-04-23T13:05:14",
            "row_create_datetime": "2019-07-04T10:00:00",
            "changed_by": "SYSTEM",
            "collection_type": "P4",
            "metering_consent": "daily_insight"
        }
    ]
    response = test_client.get("/mandate_data/", params={"mandate_id": 2})
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json() == {"mandate_data": expected_row}
