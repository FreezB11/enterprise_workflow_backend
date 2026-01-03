from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def http_error_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "path": request.url.path
        },
    )

async def generic_error_handler(request: Request, exc:Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server Error",
            "path": request.url.path
        },
    )