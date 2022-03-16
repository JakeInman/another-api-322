from array import array
from typing import Optional
from setuptools import Require
from fastapi import FastAPI
from pydantic import BaseModel
from change_calc import calculate_change
import requests

app = FastAPI()

transactions = {
    1: {
        "item_name": "apple",
        "price": 125,
        "currency_inserted": 155
    }
}

class Transaction(BaseModel):
    item_name: str
    price: int
    currency_inserted: int

@app.get("/")
def read_root():
    return {"Hello": "Please enter your item."}

@app.get("/show-transaction/{transaction_id}")
def read_item(transaction_id : int):
    if transaction_id not in transactions:
        return {"Error": "Transaction does not exist"}
    return transactions[transaction_id]  

@app.get("/make-change/{transaction_id}")
def make_change(transaction_id : int):
    return calculate_change(transactions[transaction_id]["currency_inserted"], transactions[transaction_id]["price"],  [25, 10, 5, 1])

@app.post("/make-new-item-and-change/{transaction_id}")
def make_change(transaction_id : int, transaction: Transaction):
    if transaction_id in transactions:
        return {"Error": "Transaction already exists"}
    transactions[transaction_id] = transaction
    return calculate_change(transactions[transaction_id].currency_inserted, transactions[transaction_id].price,  [25, 10, 5, 1])
