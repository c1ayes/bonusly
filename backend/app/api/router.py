from fastapi import APIRouter

from app.api import users, businesses

api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(businesses.router)