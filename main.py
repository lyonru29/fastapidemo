from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def get_root():
    return {"hello": "world"}


@app.get("/item/{item_id}")
def get_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
