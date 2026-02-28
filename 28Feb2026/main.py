from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()


class Q(Enum):
    let = "let"
    get = "get"


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/item/{item_id}")
async def update_item(item_id: int, item: Item, q: Q | None = None):
    updated_item = {"item_id": item_id, **item.model_dump()}

    if q == Q.get:
        updated_item.update({"q": q})
    elif q == Q.let:
        updated_item.update({"q": "Let in Q"})

    return updated_item
