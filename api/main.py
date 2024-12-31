from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .v1.dependencies.exceptions import InternalServerErrorException, NotFoundException
from .v1.main import router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API is running"}


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

app.include_router(router, prefix="/api/v1", tags=["API v1.0"])
