from fastapi import APIRouter
from .pool.main import router as pool_app

router = APIRouter()

router.include_router(pool_app)
