from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, Header
from pydantic import BaseModel

from App.database.session import get_db

key = "#LMAZpoqiwe"

router = APIRouter(
    prefix="/agent",
    tags=["agent"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

class Check(BaseModel):
    token_dokka: str # dokka id already inside dokka token


app = FastAPI()

@app.post("/send_heartbeat/")
async def heartsend_heartbeatbeat(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  
  return True

@app.post("/status/")
async def status(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  
  return True

@app.post("/photo/")
async def photo(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  
  return True

