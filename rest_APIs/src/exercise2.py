import uvicorn
from fastapi import FastAPI
from psycopg2.extras import RealDictCursor
from logger import setup_logger
from database_connection import database_connection
from models.mandate_data_model import MandateData
from models.response_model import Response

logger = setup_logger("mandate_data")

try:
    conn = database_connection()

    app = FastAPI()

    @app.post('/mandate_data/', response_model=Response)
    async def post_mandate_data(mandate_data: MandateData):
        cursor = conn.cursor()
        try:
            values_tuple = tuple(mandate_data.dict().values())
            logger.info(values_tuple)
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

    @app.get('/mandate_data/{mandate_id}', response_model=Response)
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
            mandate_data = MandateData(**value)
            return Response(status_code=200, message={"mandate_data": mandate_data.dict()})
        else:
            return Response(status_code=404, message="mandate_data row not found")

    @app.get('/mandate_data/', response_model=Response)
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
            mandate_data = MandateData(**value)
            return Response(status_code=200, message={"mandate_data": mandate_data.dict()})
        else:
            return Response(status_code=404, message="mandate_data row not found")

    if __name__ == "__main__":
        uvicorn.run(app, port=8080)

except Exception as e:
    logger.error(f"Error: {e}")
    raise e