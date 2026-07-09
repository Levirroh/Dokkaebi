from fastapi import APIRouter, FastAPI

from routers import dokka

app = FastAPI()

app.include_router(dokka.router)


@app.get("/{teste}")
async def read_item(teste):
    return {"item_id": teste}  