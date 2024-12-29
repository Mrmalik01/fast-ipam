from fastapi import APIRouter

router = APIRouter()

pool_data = {
    "1": {
        "pool_id": 1,
        "metadata:": {
            "business": "RetailBanking",
            "management_team_id": "B31923"
        },
        "description": "Main pool",
        "cidr": "10.0.0.10/24",
        "is_allocated": False,
        "allocation_id": None,
        "hierarchy_level": "root",
        "top_level_pool_id": 1,
        "parent_pool_id": None,
        "created_date": "2021-01-01",
        "updated_date": "2021-01-01",
        "available_pools": [
            {
                "pool_id": 1,
                "cidr": "10.0.0.0/16"
            }
        ]
    },
    "2": {
        "pool_id": 2,
        "metadata:": {
            "business": "CorporateBanking",
            "management_team_id": "Q31923"
        },
        "description": "Main pool",
        "cidr": "10.1.0.10/24",
        "is_allocated": False,
        "allocation_id": None,
        "hierarchy_level": "root",
        "top_level_pool_id": 2,
        "parent_pool_id": None,
        "created_date": "2021-01-01",
        "updated_date": "2021-01-01",
        "available_pools": [
            {
                "pool_id": 3,
                "cidr": "10.1.0.0/16"
            }
        ]
    },
    "3": {
        "pool_id": 3,
        "metadata:": {
            "business": "CorporateBanking",
            "management_team_id": "Q31923"
        },
        "description": "Main pool",
        "cidr": "10.1.0.10/28",
        "is_allocated": False,
        "allocation_id": None,
        "hierarchy_level": "sub-pool",
        "top_level_pool_id": 2,
        "parent_pool_id": 2,
        "created_date": "2021-01-01",
        "updated_date": "2021-01-01",
        "available_pools": [
            {
                "pool_id": 3,
                "cidr": "10.1.0.10/28"
            }
        ]
    }
}


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
async def get_all_pools():
    data = [pool for pool in pool_data.values()]
    print("Data: %s", data)
    return data


