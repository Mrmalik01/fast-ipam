from fastapi import APIRouter
# from .pool.main import router as pool_app
from .project.main import router as project_app

router = APIRouter()

router.include_router(project_app)