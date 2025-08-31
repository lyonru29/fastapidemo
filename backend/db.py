from typing import Generator, Optional
from sqlmodel import Session, create_engine, SQLModel, Field
from logger import logger


engine = create_engine("mysql+pymysql://root:123456@localhost/flask_demo")


SQLModel.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


class Users(SQLModel, table=True):
    __tablename__: str = "users"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
