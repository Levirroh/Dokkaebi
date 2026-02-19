from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, Header
from pydantic import BaseModel
import subprocess


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

class Phone(BaseModel):
    model: str
    android_version: str
    battery: int
    notifications: list[str]


app = FastAPI()

@app.post("/send_heartbeat/")
async def heartsend_heartbeatbeat(session = Depends(get_db)):
  
  phone = Phone(
    model=subprocess.check_output(['termux-battery-status']).decode('utf-8'),
    android_version=subprocess.run(
            ['getprop', 'ro.product.model'],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        ),
    battery=subprocess.check_output(['termux-battery-status']).decode('utf-8'),
    notifications=[]
  )

  return phone

@app.post("/status/")
async def status(session = Depends(get_db)):
  
  return True

@app.post("/photo/")
async def photo(session = Depends(get_db)):
  
  return True

