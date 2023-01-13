from typing import List

from fastapi import Depends, HTTPException, status

from database import get_session
from sqlalchemy.orm import Session

from models.posts import PostCreate, PostUpdate
from tables_model import posts_table

from configuration.logger import info_log as logger


class PostsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, post_id: int) -> posts_table.Posts:
        """ метод получения поста по id выносим для переиспользования в других методах """
        try:
            operation = (
                self.session
                .query(posts_table.Posts)
                .filter_by(id=post_id)
                .first()
            )
            if not operation:
                logger.error(f"<<< Пост с id : {post_id} не существует! {status.HTTP_404_NOT_FOUND}")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return operation
        except Exception as ex:
            logger.error(f"<<< Ошибка при получение поста :  {ex}")

    def get_list(self) -> List[posts_table.Posts]:
        """ получение списка постов """
        logger.info("<<< Start function get_list")
        try:
            operations = (
                self.session
                .query(posts_table.Posts)
                .all()
            )
            if not operations:
                logger.error(f"<<< Список постов пуст! {status.HTTP_404_NOT_FOUND}")
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return operations
        except Exception as ex:
            logger.error(f"<<< Ошибка при получение списка постов : >>> {ex}")

    def create(self, post_data: PostCreate) -> posts_table.Posts:
        """ создание нового поста """
        logger.debug(f"<<< Start function create company_data : {post_data}")
        try:
            operation = posts_table.Posts(**post_data.dict())
            self.session.add(operation)
            self.session.commit()
            return operation
        except Exception as ex:
            logger.error(f"<<< Ошибка создания поста :  {ex}")

    def get(self, post_id: int) -> posts_table.Posts:
        """ получение поста по id """
        logger.debug(f"<<< Start function get parametr post_id : {post_id}")
        return self._get(post_id)

    def update(self, post_id: int, operation_data: PostUpdate) -> posts_table.Posts:
        """ редактирование поста по id """
        logger.debug(f"<<< Start function update : post_id : {post_id}, operation_data : {operation_data}")
        try:
            operation = self._get(post_id)
            for field, value in operation_data:
                setattr(operation, field, value)
            self.session.commit()
            return operation
        except Exception as ex:
            logger.error(f"<<< Ошибка при редактирование поста :  {ex}")

    def delete(self, post_id: int):
        """  удаление поста по id """
        operation = self._get(post_id)
        self.session.delete(operation)
        self.session.commit()
