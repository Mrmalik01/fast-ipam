import uuid
from enum import Enum
from datetime import date
from typing import Union
from typing import Optional

from pydantic import BaseModel, field_validator
from pydantic_core.core_schema import ValidationInfo

from api.v1.project.core.data import ProjectModel
from api.v1.project.core.query import ProjectQuery


# Base Model for the first time created Project Object
class NewProject(BaseModel):
    project_id: str
    project_name: str
    metadata: Optional[dict] = {}
    description: Optional[str] = None
    is_production_project: bool
    created_date: date
    updated_date: date

    @field_validator('project_name', mode='before')
    def check_project_name(cls, v) -> str:
        exist_query = ProjectQuery(ProjectModel.project_name_index).query(v)
        next_item = next(exist_query, None)
        if next_item:
            raise ValueError('Project name already exists')
        return v


# Base Model for project object
class Project(BaseModel):
    project_id: str
    project_name: str
    metadata: Optional[dict] = {}
    description: Optional[str] = None
    is_production_project: bool
    created_date: date
    updated_date: date
