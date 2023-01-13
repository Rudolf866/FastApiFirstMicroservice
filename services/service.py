from sqlalchemy.orm import Session
from app.models import Post
from app.schemas import PostCreate


def get_post_list(db: Session):
    return db.query(Post).all()


def get_post_id(db: Session, ids: int):
    return db.query(Post).get(ids)


def create_post(db: Session, item: PostCreate):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
