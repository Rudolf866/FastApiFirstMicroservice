from fastapi import APIRouter

from . import (
    posts_routers,
)

router = APIRouter()

router.include_router(posts_routers.router)
