import uvicorn
from fastapi import FastAPI
from logger import setup_logger
from database_connection import database_connection
from models.response_model import Response

logger = setup_logger("meter_data")

try:
    conn = database_connection()

    app = FastAPI()

    @app.get('/meter_data/{meter_data_id}', response_model=Response)
    async def get_meter_data_by_id(meter_data_id: int):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM meter_data WHERE meter_data_id = %s", (meter_data_id,))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return Response(status_code=200, message={"meter_data": value})
        else:
            return Response(status_code=404, message="meter_data not row not found")

    @app.get('/meter_data/', response_model=Response)
    async def get_meter_data_by_query_params(business_partner_id: str):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM meter_data WHERE business_partner_id = %s", (business_partner_id,))
            value = cursor.fetchmany(2)
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return Response(status_code=200, message={"meter_data": value})
        else:
            return Response(status_code=404, message="meter_data not row not found")

    if __name__ == "__main__":
        uvicorn.run(app, port=8080)

except Exception as e:
    logger.error(f"Error: {e}")
    raise e