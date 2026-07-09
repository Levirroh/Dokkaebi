from fastapi import FastAPI

app = FastAPI()

@app.get("/{teste}")
async def read_item(teste):
    return {"item_id": teste}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}