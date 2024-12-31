from fastapi import APIRouter

from .core.models import Project
from .core.query import ProjectQuery
from .core.requests import CreateProjectRequest
from .core.services import CreateProjectService
import uuid

from ..dependencies.exceptions import PutOperationException

router = APIRouter()


@router.get("/project/{project_id}")
async def get_project_by_id(project_id: str) -> Project:
    ddb_project = ProjectQuery().get_item_by_pk(project_id)
    project = Project(**ddb_project.get_dict())
    return project

# @router.get("/pools")
# async def get_all_pools(limit: int = 10, offset: int = 0):
#     data = [pool for pool in pool_data.values()]
#     data = data[offset:offset + limit]
#     print("Data: %s", data)
#     return data


@router.post("/projects")
def create_project(request: CreateProjectRequest) -> Project:
    try:
        project = CreateProjectService(request).create()
    except PutOperationException as e:
        return {"message": str(e)}
    return project

