import pytest
import json
from testing.src import myname
from testing.src.router import get_names


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


@pytest.mark.asyncio
async def test_get_names(mocker):

    fake_rows = [
        ["Jorge", 34],
        ["David", 25],
        ["Dani", 28],
        ["Paquito", 47]
    ]

    mock_cursor = mocker.MagicMock()
    mock_cursor.fetchall.return_value = fake_rows

    mock_db = mocker.MagicMock()
    mock_db.__enter__.return_value = mock_db
    mock_db.cursor.return_value.__enter__.return_value = mock_cursor

    mocker.patch("testing.src.router.db_connection", return_value=mock_db)

    response = await get_names()

    # Used this because the method .json() is not available in lastest versions of starlette fastapi
    response_json = json.loads(response.body)

    mock_cursor.execute.assert_called_once_with("SELECT * FROM integration_test")

    # Asserts
    assert response.status_code == 200
    assert response_json == {"message": fake_rows}
