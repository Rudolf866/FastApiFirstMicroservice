from typing import List
from fastapi import APIRouter, Depends, Response, status
from models.posts import PostsBase, PostCreate, PostUpdate
from services.posts_service import PostsService

router = APIRouter(prefix="/posts")


@router.get("/", response_model=List[PostsBase])
async def company_get(service: PostsService = Depends()):
    return service.get_list()


@router.post("/", response_model=PostsBase)
def create_posts(
        post_data: PostCreate,
        service: PostsService = Depends()):
    return service.create(post_data)


@router.get("/{post_id}", response_model=PostsBase)
def get_company_id(
        post_id: int,
        service: PostsService = Depends()
):
    return service.get(post_id)


@router.put("/{post_id}", response_model=PostsBase)
def get_company_update(
        post_id: int,
        operation_data: PostUpdate,
        service: PostsService = Depends()
):
    return service.update(post_id, operation_data)


@router.delete("/{post_id}")
def company_delete(
        post_id: int,
        service: PostsService = Depends()
):
    service.delete(post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

