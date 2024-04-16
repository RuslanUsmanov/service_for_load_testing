from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["routes"])


@router.get("/hello")
def index():
    return "test"
