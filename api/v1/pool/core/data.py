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

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, MapAttribute, BooleanAttribute, ListAttribute
from api.settings import ReqEnvs


class PoolModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = ReqEnvs.POOL_TABLE_NAME.value
        # region = ReqEnvs.POOL_TABLE_REGION.value
        # aws_access_key_id = ReqEnvs.AWS_ACCESS_KEY_ID.value
        # aws_secret_access_key = ReqEnvs.AWS_SECRET_ACCESS_KEY.value
        host = "http://localhost:8000"

    pool_id = UnicodeAttribute(hash_key=True)
    pool_name = UnicodeAttribute(null=False)
    metadata = MapAttribute()
    description = UnicodeAttribute(null=True)
    cidr = UnicodeAttribute(null=False)
    is_allocated = BooleanAttribute(null=False, default=False)
    allocation_id = UnicodeAttribute(null=True)
    hierarchy_level = UnicodeAttribute(null=False)
    top_level_pool_id = UnicodeAttribute(null=False)
    parent_pool_id = UnicodeAttribute(null=True)
    created_date = UnicodeAttribute(null=False)
    updated_date = UnicodeAttribute(null=False)
    available_pools = ListAttribute(of=MapAttribute)
