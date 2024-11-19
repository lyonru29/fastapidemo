from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


class User(BaseModel):
    user_name: str


@app.get("/")
def get_root():
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
