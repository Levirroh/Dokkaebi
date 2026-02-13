from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, HTTPException, Header
from pydantic import BaseModel
import jwt

from App.database.session import get_db
from App.models.agent import Agent

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

