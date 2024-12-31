from typing import Any

import pynamodb

from api.v1.dependencies.exceptions import InternalServerErrorException, NotFoundException
from api.v1.dependencies.interfaces import QueryModelInterface
from api.v1.project.core.data import ProjectModel


class ProjectQuery(QueryModelInterface):

    def __init__(self, index=None):
        self.index = index

    def get_count(self, *args, **kwargs) -> int:
        pass

    def get_next_page(self, last_evaluated_key: str, limit: int = 10, *args, **kwargs) -> Any:
        pass

    def query(self, *args, **kwargs) -> Any:
        if self.index:
            return self.index.query(*args, **kwargs)
        return ProjectModel.query(*args, **kwargs)

    def get_item_by_pk(self, pk: str, *args, **kwargs) -> ProjectModel:
        try:
            return ProjectModel.get(hash_key=pk)
        except pynamodb.exceptions.GetError:
            raise InternalServerErrorException("Error in getting the record from the DynamoDB")
        except ProjectModel.DoesNotExist:
            raise NotFoundException(field="project_id", value=pk, message="Project not found")

    def get_item_by_pks(self, pk: str, sk: str, *args, **kwargs) -> ProjectModel:
        try:
            return ProjectModel.get(hash_key=pk, range_key=sk)
        except pynamodb.exceptions.GetError:
            raise InternalServerErrorException("Error in getting the record from the DynamoDB")
        except ProjectModel.DoesNotExist:
            raise NotFoundException(field="project_id", value=pk, message="Project not found")

    def get_all_items(self, *args, **kwargs) -> Any:
        if self.index:
            return self.index.scan()
        return ProjectModel.scan()
