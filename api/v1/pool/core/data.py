pool_data = {
    "3": {
        "pool_id": 3,
        "metadata:": {
            "business": "CorporateBanking",
            "management_team_id": "Q31923"
        },
        "description": "Main pool",
        "cidr": "10.1.0.10/28",
        "hierarchy_level": "sub-pool",
        "parent_pool_id": 2,
        "created_date": "2021-01-01",
        "updated_date": "2021-01-01",
        "allocated_sub_pools": {
            "10.1.0.0.10/30": 4
        },
        "allocated_resources": {
            "10.1.0.0.50/32": "R122D32"
        }
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
    hierarchy_level = UnicodeAttribute(null=False)
    parent_pool_id = UnicodeAttribute(null=True)
    allocated_sub_pools = MapAttribute()
    allocated_resources = MapAttribute()
    created_date = UnicodeAttribute(null=False)
    updated_date = UnicodeAttribute(null=False)
