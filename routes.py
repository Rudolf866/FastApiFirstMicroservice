from fastapi import APIRouter
from app import blog

routes = APIRouter()

routes.include_router(blog.router, prefix="/blog")