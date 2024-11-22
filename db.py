from typing import Generator, Optional
from sqlmodel import Session, create_engine, SQLModel, Field
from logger import logger
logger.info("ss")

engine = create_engine("mysql+pymysql://root:123456@localhost/flask_demo")





SQLModel.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
