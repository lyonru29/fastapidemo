from fastapi import APIRouter

from app.routers import auth

router = APIRouter(prefix="/api", tags=["main"])

router.include_router(auth.router)