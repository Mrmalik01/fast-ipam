from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError, BaseModel

from api.v1.dependencies.exceptions import InternalServerErrorException, NotFoundException

from api.main import app


# class ValidationError(BaseModel):
#     detail
#     errors: list


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    errors = []
    for e in exc.errors():
        if "input" in e:
            e['input'] = str(e['input'])
        if "ctx" in e and "error" in e['ctx']:
            e['ctx']['error'] = str(e['ctx']['error'])
        e.pop("url", None)
        errors.append(e)
    return JSONResponse(
        status_code=422,
        content={"detail": "Validation Error", "status_code": 422, "errors": errors},
    )


@app.exception_handler(InternalServerErrorException)
async def validation_exception_handler(request: Request, exc: InternalServerErrorException):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error", "status_code": 500},
    )


@app.exception_handler(NotFoundException)
async def validation_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"detail": "Not Found",
                 "status_code": 404,
                 "error": {
                     "field": exc.field,
                     "value": exc.value,
                     "message": exc.message}})