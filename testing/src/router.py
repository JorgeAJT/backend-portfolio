from fastapi import APIRouter
from fastapi.responses import JSONResponse
from psycopg2.extras import DictCursor
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