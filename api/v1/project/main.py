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
    project = ProjectQuery().get_item_by_pk(project_id)
    payload = Project(**project.get_dict())
    return payload

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
        payload = Project(**project.get_dict())
    except PutOperationException as e:
        return {"message": str(e)}
    return payload

