from typing import Union, Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlmodel import Session
from db import get_db
from logger import logger
app = FastAPI()


SessionDep = Annotated[Session, Depends(get_db)]


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
    user: User = User(user_name="11")
    sesssion.add(user)
    sesssion.commit()
    sesssion.flush()
