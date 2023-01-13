from sqlalchemy import (
    MetaData,
    create_engine,
)
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine(settings.database_url)

Session = sessionmaker(
    engine,
    autocommit=False,
    autoflush=False,
)

""" пример внедрения зависимостей """


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


metadata = MetaData(schema="public")
# users = Table("users", metadata, autoload_with=engine)
# company = Table("company", metadata, autoload_with=engine)
