from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    available: bool = True

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {
        "item_id": item_id,
        "q": q,
        "message": "Item retrieved successfully"
    }

@app.post("/items/")
def create_item(item: Item):
    return {
        "message": "Item created successfully",
        "item": item
    }
