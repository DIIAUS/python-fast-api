from typing import Union
from fastapi import FastAPI
from models.itemModel import Item

app = FastAPI(title='My API', version='0.1.0', summary='My first fastapi app' )


@app.get("/")
async def read_root():
    return "this is python fast api"

@app.get("/items/{itemId}", tags=['items'])
async def read_item(itemId: int, q: Union[str, None] = None):
    return {"itemId": itemId, "q": q}

@app.put("/items/{itemId}", response_model = Item, tags=['items'])
def updateItem(itemId: int, item: Item):
    return {"itemName": item.name, "itemId": itemId}