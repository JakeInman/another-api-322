from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from change_calc import calculate_change

app = FastAPI()

class Transaction(BaseModel):
    item_name: str
    price: int
    currency_inserted: int

class UpdateTransaction(BaseModel):
    item_name: Optional[str] = None
    price: Optional[int] = None
    currency_insterted: Optional[int] = None

transactions = {
    1: Transaction(item_name="apple", price=125, currency_inserted=155)
}

@app.get("/")
def read_root():
    return {
        "status": "Successful Login",
        "message": "Hello, please enter your item."
        }

@app.get("/show-transaction/{transaction_id}")
def read_item(transaction_id : int):
    if transaction_id not in transactions:
        return {
            "status": "ERROR: Transaction Not Found",
            "message": "Sorry, we could not locate that transaction."
            }
    return transactions[transaction_id]  

@app.get("/make-change/{transaction_id}")
def make_change(transaction_id : int):
    if transaction_id not in transactions:
        return {
            "status": "ERROR: Transaction Not Found",
            "message": "Sorry, we could not locate that transaction."
            }
    return calculate_change(transactions[transaction_id].currency_inserted, transactions[transaction_id].price,  [25, 10, 5, 1])

@app.post("/make-new-item-and-change/{transaction_id}")
def make_change(transaction_id : int, transaction: Transaction):
    if transaction_id in transactions:
        return {
            "status": "ERROR: Transaction Already Exists",
            "messsage": "Sorry, that transaction already exists."
            }
    transactions[transaction_id] = transaction
    return calculate_change(transactions[transaction_id].currency_inserted, transactions[transaction_id].price,  [25, 10, 5, 1])

@app.put("/update-transaction/{transaction_id}")
def update_transaction(transaction_id: int, transaction: UpdateTransaction):
    if transaction_id not in transactions:
        return {
            "status": "ERROR: Transaction Not Found",
            "message": "Sorry, we could not locate that transaction."
            }

    if transaction.item_name != None:
        transactions[transaction_id].item_name = transaction.item_name

    if transaction.price != None:
        transactions[transaction_id].price = transaction.price

    if transaction.currency_insterted != None:
        transactions[transaction_id].currency_inserted = transaction.currency_insterted

    return transactions[transaction_id]

@app.delete("/delete-transaction/{transaction_id}")
def delete_transaction(transaction_id: int):
    if transaction_id not in transactions:
        return {
            "status": "ERROR: Transaction Not Found",
            "message": "Sorry, we could not locate that transaction."
            }
    del transactions[transaction_id]
    return{
        "status": "Successful Deletion",
        "message": "Transaction deleted successfully."
        }
