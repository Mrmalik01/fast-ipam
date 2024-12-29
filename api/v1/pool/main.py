from fastapi import APIRouter
from .models import CreatePoolRequest
from .data import pool_data
import uuid

router = APIRouter()


@router.get("/pool/{pool_id}")
async def get_pool_by_id(pool_id: str):
    print("pool_id: %s", pool_id)
    pool = pool_data.get(pool_id)
    if pool:
        return pool
    return {"message": "Pool not found"}


@router.delete("/pool/{pool_id}")
async def delete_pool_by_id(pool_id: str):
    pool = pool_data.get(pool_id)
    if not pool:
        return {"message": "Pool not found"}
    pool_data.pop(pool_id)
    if pool:
        return pool


@router.get("/pools")
async def get_all_pools(limit: int = 10, offset: int = 0):
    data = [pool for pool in pool_data.values()]
    data = data[offset:offset + limit]
    print("Data: %s", data)
    return data


@router.post("/pools")
async def create_pool(pool: CreatePoolRequest):
    print("Pool: %s", pool)
    pool_id = str(uuid.uuid4())



    return {"message": "Pool created"}

