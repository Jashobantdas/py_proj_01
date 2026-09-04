from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from starlette.exceptions import HTTPException as StarletteHTTPException

from configs.custom_exception import BusinessException


def register_exception_handlers(app):

    # Business exceptions
    @app.exception_handler(BusinessException)
    async def business_exception_handler(
        request: Request,
        exc: BusinessException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": exc.status_code,
                "message": exc.message
            }
        )


    # Request validation errors (Swagger input errors)
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):
        return JSONResponse(
            status_code=422,
            content={
                "status": 422,
                "message": "Validation error",
                "errors": exc.errors()
            }
        )


    # FastAPI/Starlette HTTP exceptions
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request,
        exc: StarletteHTTPException
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": exc.status_code,
                "message": exc.detail
            }
        )


    # Database exceptions
    @app.exception_handler(SQLAlchemyError)
    async def database_exception_handler(
        request: Request,
        exc: SQLAlchemyError
    ):
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "message": "Database error"
            }
        )


    # Any unknown/unhandled exception
    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception
    ):
        return JSONResponse(
            status_code=500,
            content={
                "status": 500,
                "message": "Internal server error"
            }
        )