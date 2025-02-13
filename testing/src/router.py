from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from psycopg2.extras import RealDictCursor, DictCursor
from testing.src.utils import db_connection

router = APIRouter()


@router.get("/hello/")
async def get_say_hello() -> JSONResponse:
    return JSONResponse(content={"message": "hello Jorge"}, status_code=200)


@router.get("/names/")
async def get_names() -> JSONResponse:
    with db_connection() as pg_conn:
        with pg_conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("SELECT * FROM integration_test")
            records = cursor.fetchall()

    return JSONResponse(content={"message": records}, status_code=200)


@router.get('/mandate_data/')
async def get_mandate_data(mandate_id: int) -> JSONResponse:
    with db_connection() as pg_conn:
        with pg_conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute('SELECT * FROM mandate_data WHERE mandate_id = %s', (mandate_id,))
            records = cursor.fetchall()

            # jsonable_encoder to convert complex structures like datetimes in other structures compatible with JSON
            encoded_data = jsonable_encoder({"mandate_data": records})

    return JSONResponse(content=encoded_data, status_code=200)
