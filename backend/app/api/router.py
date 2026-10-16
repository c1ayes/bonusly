from fastapi import APIRouter

from app.api import users, businesses, user_business, rewards, reward_redemptions

api_router = APIRouter()

api_router.include_router(users.router)
api_router.include_router(businesses.router)
api_router.include_router(user_business.router)
api_router.include_router(rewards.router)
api_router.include_router(reward_redemptions.router)