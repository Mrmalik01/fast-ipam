from enum import Enum
import os


class ReqEnvs(str, Enum):
    POOL_TABLE_NAME = os.getenv("POOL_TABLE_NAME")
    POOL_TABLE_REGION = os.getenv("POOL_TABLE_REGION")
    RESOURCE_ALLOCATION_TABLE_NAME = os.getenv("RESOURCE_ALLOCATION_TABLE_NAME")
    RESOURCE_ALLOCATION_TABLE_REGION = os.getenv("RESOURCE_ALLOCATION_TABLE_REGION")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET")