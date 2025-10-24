from typing import Generator, Optional

from sqlmodel import Field, Session, SQLModel, create_engine

engine = create_engine("mysql+pymysql://root:scrm1561@8.134.195.150/flask_demo")

SQLModel.metadata.create_all(engine)


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


def add(a:int, b:int) -> int:
    return a + b
