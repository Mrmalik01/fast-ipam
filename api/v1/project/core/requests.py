from pydantic import BaseModel
from pydantic import BaseModel, Field
from typing import Optional


class CreateProjectRequest(BaseModel):
    project_name: str
    metadata: Optional[dict] = {}
    description: Optional[str] = None
    is_production_project: bool
