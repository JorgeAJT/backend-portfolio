from fastapi import APIRouter
from rest_APIs.src.utils import setup_logger, database_connection

logger = setup_logger("meter-readings")

try:
    conn = database_connection()

    meter_readings_router = APIRouter()

    @meter_readings_router.get('/meter_readings/{meter_readings_id}')
    async def get_meter_reading_by_query_params(meter_readings_id: int):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM meter_readings WHERE meter_readings_id = %s", (meter_readings_id, ))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning meter_readings row", "meter_reading": value}}
        else:
            return {"status_code": 404, "body": {"message": "meter_reading not found"}}

    @meter_readings_router.get('/meter_readings/')
    async def get_meter_reading_by_query_params(meter_number: str, account_id: str, energy_type: str):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM meter_readings WHERE meter_number = %s AND account_id = %s AND energy_type = %s", (meter_number, account_id, energy_type))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning meter_readings row", "meter_reading": value}}
        else:
            return {"status_code": 404, "body": {"message": "meter_reading not found"}}

except Exception as e:
    logger.error(f"Error: {e}")
    raise e