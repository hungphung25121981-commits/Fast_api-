from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

fake_db = []

@app.post("/items")
def create_item(item: Item):
    fake_db.append(item)
    return {
        "message": "tao thanh cong",
        "tong_so_mon": len(fake_db),
        "data": item
    }

@app.get("/items/{item_id}")
def read_item(item_id: int):
   
    if item_id < 0 or item_id >= len(fake_db):
        return {
            "error": f"Khong tim thay item_id={item_id}. Hien tai kho chi co {len(fake_db)} mon (hay POST truoc!)."
        }
        
    return {
        "item_id": item_id,
        "item_info": fake_db[item_id]
    }