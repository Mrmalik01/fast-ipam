import uuid
from enum import Enum
from datetime import date
from pydantic import BaseModel


class HierarchyLevel(str, Enum):
    root = "root"
    sub_pool = "sub-pool"


class CreatePoolRequest(BaseModel):
    name: str
    metadata: dict | {}
    description: str | None
    cidr: str
    hierarchy_level: HierarchyLevel
    top_level_pool_id: uuid.UUID | None
    parent_pool_id: uuid.UUID | None


class AvailablePool(BaseModel):
    pool_id: uuid.UUID
    cidr: str


class Pool(BaseModel):
    pool_id: uuid.UUID
    pool_name: str
    metadata: dict | {}
    description: str | None
    cidr: str
    is_allocated: bool
    allocation_id: uuid.UUID | None
    hierarchy_level: HierarchyLevel
    top_level_pool_id: uuid.UUID
    parent_pool_id: uuid.UUID | None
    created_date: date
    updated_date: date
    available_pools: AvailablePool
