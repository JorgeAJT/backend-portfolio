from fastapi import APIRouter
from .routes import meter_readings_router, mandate_data_router, meter_data_router

api_router = APIRouter()
api_router.include_router(meter_readings_router)
api_router.include_router(mandate_data_router)
api_router.include_router(meter_data_router)