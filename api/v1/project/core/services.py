from datetime import datetime
from typing import Any
import pynamodb

from pydantic.v1 import ValidationError

from api.settings import settings
from api.v1.project.core.models import Project, NewProject
from api.v1.project.core.requests import CreateProjectRequest
from api.v1.dependencies.interfaces import CreateModelInterface, UpdateModelInterface
import uuid

from .query import ProjectQuery
from ..core.data import ProjectModel
from ...dependencies.exceptions import PutOperationException, InternalServerErrorException, NotFoundException, \
    BadRequestException

def _generate_unique_id() -> str:
    while True:
        _id = uuid.uuid4().__str__()
        try:
            ProjectQuery().get_item_by_pk(_id)
            continue
        except NotFoundException as ex:
            print("Error: %s", ex)
            return _id


class CreateProjectService(CreateModelInterface):

    def __init__(self, request: CreateProjectRequest):
        self.request = request

    def _validate(self, project_item: dict, *args, **kwargs):
        _project = NewProject(**project_item)

    def create(self) -> ProjectModel:
        _id = _generate_unique_id()
        _project_dict = self.request.model_dump()
        _project_dict['project_id'] = _id
        _project_dict['created_date'] = datetime.now().date().__str__()
        _project_dict['updated_date'] = datetime.now().date().__str__()
        self._validate(_project_dict)
        print("Validation Completed: %s", _project_dict)
        project = ProjectModel(**_project_dict)

        try:
            project.save()
        except pynamodb.exceptions.PutError as e:
            print("Error: %s", e)
            raise PutOperationException("Error in creating the record in the DynamoDB")
        return project
