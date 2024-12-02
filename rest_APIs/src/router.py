from fastapi import APIRouter
from .routes import general_data_router

api_router = APIRouter()
api_router.include_router(general_data_router)