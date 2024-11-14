from fastapi import APIRouter
from login_service import router as login_router

main_router = APIRouter()
main_router.include_router(login_router)