import uvicorn
import logging
from fastapi import FastAPI
from database_connection import database_connection
from models.mandate_data_model import MandateData

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    conn = database_connection()

    app = FastAPI()

    @app.post('/mandate_data/')
    async def post_mandate_data(mandate_data: MandateData):
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO mandate_data (
                    mandate_id, business_partner_id, brand, mandate_status,
                    collection_frequency, row_update_datetime, row_create_datetime,
                    changed_by, collection_type, metering_consent
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                mandate_data.mandate_id, mandate_data.business_partner_id, mandate_data.brand,
                mandate_data.mandate_status, mandate_data.collection_frequency,
                mandate_data.row_update_datetime, mandate_data.row_create_datetime,
                mandate_data.changed_by, mandate_data.collection_type, mandate_data.metering_consent
            ))
            conn.commit()
            return {"status_code": 201,
                    "body": {"message": f"Request {mandate_data.mandate_id} was created successfully"}}
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            return {"status_code": 404, "body": {"message": "mandate_data wasn't correct"}}
        finally:
            cursor.close()

    @app.get('/mandate_data/{mandate_id}')
    async def get_mandate_data_by_id(mandate_id: int):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM mandate_data WHERE mandate_id = %s", (mandate_id,))
            value = cursor.fetchone()
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning mandate_data row", "mandate_data": value}}
        else:
            return {"status_code": 404, "body": {"message": "mandate_data not found"}}

    @app.get('/mandate_data/')
    async def get_mandate_data_by_query_params(business_partner_id: str, mandate_status: str):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM mandate_data WHERE business_partner_id = %s AND mandate_status = %s", (business_partner_id,mandate_status))
            value = cursor.fetchone()
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning mandate_data row", "mandate_data": value}}
        else:
            return {"status_code": 404, "body": {"message": "mandate_data not found"}}

    if __name__ == "__main__":
        uvicorn.run(app, port=8080)

except Exception as e:
    logging.error(f"Error: {e}")
    raise e