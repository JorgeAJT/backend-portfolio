from fastapi import APIRouter
from psycopg2.extras import RealDictCursor
from rest_APIs.src.utils import setup_logger, database_connection
from rest_APIs.src.models import MandateData, Response

logger = setup_logger("mandate-data")

try:
    conn = database_connection()

    mandate_data_router = APIRouter()

    @mandate_data_router.post('/mandate_data/', response_model=Response)
    async def post_mandate_data(mandate_data: MandateData):
        cursor = conn.cursor()
        try:
            values_tuple = tuple(mandate_data.dict().values())
            cursor.execute("""
                INSERT INTO mandate_data (
                    mandate_id, business_partner_id, brand, mandate_status,
                    collection_frequency, row_update_datetime, row_create_datetime,
                    changed_by, collection_type, metering_consent
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, values_tuple)
            conn.commit()
            return Response(status_code=201,
                            message={"mandate_data": mandate_data.dict()})
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            return Response(status_code=400, message="mandate_data wasn't correct")
        finally:
            cursor.close()

    @mandate_data_router.get('/mandate_data/{mandate_id}', response_model=Response)
    async def get_mandate_data_by_id(mandate_id: int):
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute("SELECT * FROM mandate_data WHERE mandate_id = %s", (mandate_id,))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return Response(status_code=200, message={"mandate_data": value})
        else:
            return Response(status_code=404, message="mandate_data row not found")

    @mandate_data_router.get('/mandate_data/', response_model=Response)
    async def get_mandate_data_by_query_params(business_partner_id: str, mandate_status: str):
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            cursor.execute("SELECT * FROM mandate_data WHERE business_partner_id = %s AND mandate_status = %s",
                           (business_partner_id,mandate_status))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return Response(status_code=200, message={"mandate_data": value})
        else:
            return Response(status_code=404, message="mandate_data row not found")

except Exception as e:
    logger.error(f"Error: {e}")
    raise e