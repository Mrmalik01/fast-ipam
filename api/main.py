from fastapi import FastAPI
from .v1.main import router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is running"}

app.include_router(router, prefix="/api/v1", tags=["API v1.0"])
