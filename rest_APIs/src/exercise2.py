import uvicorn
import logging
from fastapi import FastAPI
from pydantic import BaseModel
from rest_APIs.src.database_connection import database_connection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    conn = database_connection()

    app = FastAPI()

    class MandateData(BaseModel):
        mandate_id: int
        business_partner_id: str
        brand: str
        mandate_status: str
        collection_frequency: str
        row_update_datetime: str
        row_create_datetime: str
        changed_by: str
        collection_type: str
        metering_consent: str


    @app.post('/mandate_data/')
    async def post_mandate_data(mandate_data: MandateData):
        # Creates a Meter Data Row data: str -> query parameter
        cursor = conn.cursor()
        try:
            cursor.execute(f"INSERT INTO mandate_data VALUES({mandate_data})")
            cursor.close()
            return {"status_code": 200,
                    "body": {"message": f"Request {mandate_data.mandate_id} was created successfully"}}
        except Exception as e:
            logging.error(f"Error executing query: {e}")
            cursor.close()
            return {"status_code": 404, "body": {"message": "mandate_data wasn't correct"}}


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