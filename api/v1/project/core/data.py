from pynamodb.indexes import GlobalSecondaryIndex
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, MapAttribute, BooleanAttribute, ListAttribute
from pynamodb.indexes import KeysOnlyProjection
from api.settings import settings


class ProjectNameIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = settings.project_table_gsi_project_name
        projection = KeysOnlyProjection()

    project_name = UnicodeAttribute(hash_key=True)


class ProjectModel(Model):
    """
    A DynamoDB User
    """
    class Meta:
        table_name = settings.project_table_name
        if settings.env == "local":
            host = "http://localhost:8000"
        else:
            region = settings.aws_region
            aws_access_key_id = settings.aws_access_key_id
            aws_secret_access_key = settings.aws_secret_access_key

    project_id = UnicodeAttribute(hash_key=True)
    project_name = UnicodeAttribute(null=True)
    metadata = MapAttribute()
    description = UnicodeAttribute(null=True)
    is_production_project = BooleanAttribute(null=False)
    created_date = UnicodeAttribute(null=False)
    updated_date = UnicodeAttribute(null=False)

    # GSI partition key
    project_name_index = ProjectNameIndex()

    def get_dict(self):
        return {
            "project_id": self.project_id,
            "project_name": self.project_name,
            "metadata":  self.metadata.as_dict(),
            "description": self.description,
            "is_production_project": self.is_production_project,
            "created_date": self.created_date,
            "updated_date": self.updated_date
        }

