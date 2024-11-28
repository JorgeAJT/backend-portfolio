import uvicorn
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from logger import setup_logger
from database_connection import database_connection
from models.response_model import Response
from models.meter_data_model import MeterDataResponse

logger = setup_logger("meter_data")

try:
    conn = database_connection()

    app = FastAPI()

    @app.get('/meter_data/{meter_data_id}', response_model=Response)
    async def get_meter_data_by_id(meter_data_id: int):
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute("SELECT * FROM meter_data WHERE meter_data_id = %s", (meter_data_id,))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            meter_data = MeterDataResponse(**value)
            return Response(status_code=200, message={"meter_data": meter_data.dict()})
        else:
            return Response(status_code=404, message="meter_data row not found")

    @app.get('/meter_data/', response_model=Response)
    async def get_meter_data_by_query_params(business_partner_id: str):
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute("SELECT * FROM meter_data WHERE business_partner_id = %s", (business_partner_id,))
            values = cursor.fetchmany(2)
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            values = None
        finally:
            cursor.close()

        if values:
            return Response(status_code=200, message={"meter_data": values})
        else:
            return Response(status_code=404, message="meter_data row not found")

    if __name__ == "__main__":
        uvicorn.run(app, port=8080)

except Exception as e:
    logger.error(f"Error: {e}")
    raise e