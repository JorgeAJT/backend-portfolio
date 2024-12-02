from fastapi import APIRouter
from rest_APIs.src.utils import setup_logger, database_connection

logger = setup_logger("general-data")

try:
    conn = database_connection()

    general_data_router = APIRouter()

    @general_data_router.get('/meter_data/{meter_data_id}')
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
            return {"status_code": 200, "body": {"message": "Returning meter_data row", "meter_data": value}}
        else:
            return {"status_code": 404, "body": {"message": "meter_data not found"}}

    @general_data_router.get('/meter_data/')
    async def get_meter_data_by_query_params(connection_ean_code: str, business_partner_id: str):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM meter_data WHERE connection_ean_code = %s AND business_partner_id = %s", (connection_ean_code,business_partner_id))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning meter_data row", "meter_data": value}}
        else:
            return {"status_code": 404, "body": {"message": "meter_data not found"}}

    @general_data_router.get('/mandate_data/{mandate_id}')
    async def get_mandate_data_by_id(mandate_id: int):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM mandate_data WHERE mandate_id = %s", (mandate_id,))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning mandate_data row", "mandate_data": value}}
        else:
            return {"status_code": 404, "body": {"message": "mandate_data not found"}}

    @general_data_router.get('/mandate_data/')
    async def get_mandate_data_by_query_params(business_partner_id: str, mandate_status: str):
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM mandate_data WHERE business_partner_id = %s AND mandate_status = %s", (business_partner_id,mandate_status))
            value = cursor.fetchone()
        except Exception as e:
            logger.error(f"Error executing query: {e}")
            value = None
        finally:
            cursor.close()

        if value:
            return {"status_code": 200, "body": {"message": "Returning mandate_data row", "mandate_data": value}}
        else:
            return {"status_code": 404, "body": {"message": "mandate_data not found"}}

    @general_data_router.get('/meter_readings/')
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