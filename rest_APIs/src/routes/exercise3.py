from fastapi import APIRouter
from psycopg2.extras import RealDictCursor
from rest_APIs.src.utils import setup_logger, database_connection
from rest_APIs.src.models import Response

logger = setup_logger("meter-data")

try:
    conn = database_connection()

    meter_data_router = APIRouter()

    @meter_data_router.get('/meter_data/{meter_data_id}', response_model=Response)
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
            return Response(status_code=200, message={"meter_data": value})
        else:
            return Response(status_code=404, message="meter_data row not found")

    @meter_data_router.get('/meter_data/', response_model=Response)
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

except Exception as e:
    logger.error(f"Error: {e}")
    raise e