import asyncio
from random import gauss, uniform

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

router = APIRouter(prefix="/api", tags=["routes"])


class CustomResp(BaseModel):
    message: str


@router.get("/fast", response_model=CustomResp)
async def fast():
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )


@router.get("/slow", response_model=CustomResp)
async def slow():
    await asyncio.sleep(1)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )


@router.get("/slower", response_model=CustomResp)
async def slower():
    await asyncio.sleep(5)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )


@router.get("/slowest", response_model=CustomResp)
async def slowest():
    await asyncio.sleep(10)
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )


@router.get("/slow_with_deviation")
async def slow_with_deviation():
    await asyncio.sleep(5 + gauss(0, 2))
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )


@router.get("/random", response_model=CustomResp)
async def random():
    await asyncio.sleep(uniform(0, 10))
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )


@router.get("/random_gauss", response_model=CustomResp)
async def random_with_deviation():
    await asyncio.sleep(gauss(3, 2))
    return JSONResponse(
        status_code=status.HTTP_200_OK, content={"message": "OK"}
    )
