import uuid
from enum import Enum
from datetime import date
from pydantic import BaseModel

############################################################################################################
# Note:
#   - Pool and Sub Pool are the same thing.
#   - This is a design decision to create separate endpoints for the same object for better validation
############################################################################################################


class HierarchyLevel(str, Enum):
    root = "root"
    sub_pool = "sub-pool"


# Base Model for the Create Pool Request
class CreatePoolRequest(BaseModel):
    name: str
    metadata: dict | {}
    description: str | None
    cidr: str
    hierarchy_level: HierarchyLevel


# Base Model for the Create Sub Pool Request
class CreateSubPoolRequest(BaseModel):
    name: str
    metadata: dict | {}
    description: str | None
    cidr: str
    hierarchy_level: HierarchyLevel
    parent_pool_id: uuid.UUID


# Base Model for the Pool Object
class Pool(BaseModel):
    pool_id: uuid.UUID
    pool_name: str
    metadata: dict | {}
    description: str | None
    cidr: str
    start_ip_address: int
    end_ip_address: int
    hierarchy_level: HierarchyLevel
    parent_pool_id: uuid.UUID | None
    allocated_sub_pools: dict[str, uuid.UUID] | {}
    allocated_resources: dict[str, uuid.UUID] | {}
    created_date: date
    updated_date: date
