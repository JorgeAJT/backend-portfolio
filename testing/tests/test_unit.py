import pytest
import json
from testing.src import myname
from testing.src.router import get_names, get_mandate_data


def test_myname():
    res = myname("Jorge")
    assert res == "Jorge"


def test_myname_null():
    res = myname(None)
    assert res == "Not a valid name"


def test_myname_list():
    res_empty = myname([])
    res = myname(["Jorge"])
    assert res_empty == "Not a valid name"
    assert res == "Not a valid name"


def test_myname_tuples():
    res_empty = myname(())
    res = myname(("Jorge", ))
    assert res_empty == "Not a valid name"
    assert res == "Not a valid name"


def test_myname_dictionary():
    res_empty = myname({})
    res = myname({"name": "Jorge"})
    assert res_empty == "Not a valid name"
    assert res == "Not a valid name"


@pytest.mark.asyncio # This decorator says that the function is async
async def test_get_names(mocker): # mocker is a fixture to create simulated objects and patches

    fake_rows = [
        ["Jorge", 34],
        ["David", 25],
        ["Dani", 28],
        ["Paquito", 47]
    ]

    # Created cursor mock
    mock_cursor = mocker.MagicMock()

    # Say to the mock when someone calls cursor.fetchall() use fake_rows as a response
    mock_cursor.fetchall.return_value = fake_rows

    # Created db connection mock
    mock_db = mocker.MagicMock()

    # "with" behavior is imitated here doing __enter__() returning us the same connection in the same variable
    mock_db.__enter__.return_value = mock_db

    # mock_db.cursor.return_value is the object which is made when your code executes pg_conn.cursor()
    mock_db.cursor.return_value.__enter__.return_value = mock_cursor

    # Every time db_connection() is called, use mock_db instead of the real connection
    mocker.patch("testing.src.router.db_connection", return_value=mock_db)

    response = await get_names()

    # Used this because the method .json() is not available in lastest versions of starlette fastapi
    response_json = json.loads(response.body)

    # It's a check of what happened in get_names()
    mock_cursor.execute.assert_called_once_with("SELECT * FROM integration_test")

    # Asserts
    assert response.status_code == 200
    assert response_json == {"message": fake_rows}

@pytest.mark.asyncio
async def test_get_mandate_data(mocker):

    fake_row =  [
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

    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = fake_row

    mock_db = mocker.MagicMock()
    mock_db.__enter__.return_value = mock_db
    mock_db.cursor.return_value.__enter__.return_value = mock_cursor

    mocker.patch("testing.src.router.db_connection", return_value=mock_db)

    response = await get_mandate_data(2)

    response_json = json.loads(response.body)

    mock_cursor.execute.assert_called_once_with('SELECT * FROM mandate_data WHERE mandate_id = %s', (2,))

    assert response.status_code == 200
    assert response_json == {"mandate_data": fake_row}





