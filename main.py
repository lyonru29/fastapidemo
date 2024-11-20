from typing import Union, Generator, Annotated, Optional

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlmodel import create_engine, Field, Session, SQLModel
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi")
logger.info("server starting...")
engine = create_engine("mysql+pymysql://root:123456@localhost/flask_demo")


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


app = FastAPI()
SessionDep = Annotated[Session, Depends(get_db)]


class Users(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


SQLModel.metadata.create_all(engine)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    user_name: str


@app.get("/")
def get_root():
    logger.info("hello")
    return {"hello": "world"}


@app.get("/item/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.post("/item2/{item_id}")
def save_item(item_id: int, item: Item, user: User):
    return {"item_name": item.name, "item_id": item_id, "user": user}


@app.post("/item3/get", response_model=User)
def save_item2(item_id: int, item: Item, user: User):
    return user


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.post("/depends/get")
def depends(common: CommonQueryParams = Depends(CommonQueryParams)):
    return {}


@app.post("/save_user")
def save_user(sesssion: SessionDep):
    user = Users()
    user.name = "11"
    user.id = 1
    sesssion.add(user)
    sesssion.commit()
    sesssion.flush()
