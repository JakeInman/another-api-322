from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from change_calc import calculate_change

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None

class Cart(BaseModel):
    item_list: list
    item_count: int
    total_cost: int
    currency_inserted: int

class UpdateCart(BaseModel):
    item_list: Optional[list] = None
    item_count: Optional[int] = None
    total_cost: Optional[int] = None
    currency_insterted: Optional[int] = None

items = {
    1: Item(name="apple", price=125),
    2: Item(name="orange", price=200)
}

carts = {
    1: Cart(item_list = [{"name": "apple", "price": 125}, {"name": "apple", "price": 125}, {"name": "orange", "price": 200}], item_count=3, total_cost=450, currency_inserted=600)
}

@app.get("/")
def read_root():
    return {
        "status": "Successful Login",
        "message": "Hello, please enter your item."
        }

@app.get("/show-item/{item_id}")
def read_item(item_id : int):
    if item_id not in items:
        return {
            "status": "ERROR: Item Not Found",
            "message": "Sorry, we could not locate that item."
            }
    return items[item_id]

@app.get("/view-cart")
def view_cart(cart_id: int):
    if carts[cart_id].item_count == 0:
        return {
            "status": "ERROR: Cart Is Empty",
            "message": "Sorry, we could not locate any items in your cart."
            }
    return carts[cart_id]

@app.get("/checkout")
def checkout(cart_id: int):
    if carts[cart_id] == 0:
        return {
            "status": "ERROR: Cart Is Empty",
            "message": "Sorry, we could not locate any items in your cart."
            }
    return calculate_change(carts[cart_id].currency_inserted, carts[cart_id].total_cost,  [25, 10, 5, 1])

@app.post("/make-new-item/{item_id}")
def make_new_item(item_id : int, item: Item):
    if item_id in items:
        return {
            "status": "ERROR: Item Already Exists",
            "messsage": "Sorry, that item already exists."
            }
    items[item_id] = item
    return item

@app.post("/add-item-to-cart/{item_id}")
def add_item_to_cart(item_id: int, cart_id: int):
    if item_id not in items:
        return {
            "status": "ERROR: Item Not Found",
            "message": "Sorry, we could not locate that item."
            }
    carts[cart_id].item_list.append(items[item_id])
    return carts[cart_id]


@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in items:
        return {
            "status": "ERROR: Item Not Found",
            "message": "Sorry, we could not locate that item."
            }

    if item.name != None:
        items[item_id].name = item.name

    if item.price != None:
        items[item_id].price = item.price

    return items[item_id]

@app.delete("/delete-item/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        return {
            "status": "ERROR: Item Not Found",
            "message": "Sorry, we could not locate that item."
            }
    del items[item_id]
    return{
        "status": "Successful Deletion",
        "message": "Item deleted successfully."
        }
