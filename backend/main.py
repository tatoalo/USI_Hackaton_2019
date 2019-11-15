from fastapi import FastAPI
import classes as c

app = FastAPI()

bus16 = {"item_id":16,"ID":1,"address":"Pocomaco","price":20}



@app.post("/items/")
async def create_item(item: c.Bus):
    return item

a = create_item(bus16)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return Buss(**data)

@app.put("/items/{item_id}")
def update_item(item_id: int, item: c.Bus):
    return {"item_name": item.name, "item_id": item_id}
