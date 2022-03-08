from array import array
from typing import Optional
from setuptools import Require
from fastapi import FastAPI
from pydantic import BaseModel
from change_calc import calculate_change
import requests

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Optional[bool] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.post("/change")
# def make_change():
#     return calculate_change(500, 325, [25, 10, 5, 1])
r = requests.post("http://127.0.0.1:8000/change", calculate_change(500, 325, [25, 10, 5, 1]))
print(r)