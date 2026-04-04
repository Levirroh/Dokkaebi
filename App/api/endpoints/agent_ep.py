import json
from typing import Optional
from fastapi import APIRouter, Depends, FastAPI, HTTPException
import httpx
from pydantic import BaseModel
import subprocess

from dotenv import load_dotenv
import os
load_dotenv()


key = os.getenv("DOKKA_KEY")
ip_dokka = os.getenv("IP_DOKKA")



from database.session import get_db

router = APIRouter(
    prefix="/agent",
    tags=["agent"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

class Check(BaseModel):
    token_dokka: str # dokka id already inside dokka token

class Battery(BaseModel):
  present: Optional[bool]
  technology: Optional[str]
  health: Optional[str]
  plugged: Optional[str]
  status: Optional[str]
  voltage: Optional[int]
  current: Optional[int]
  current_average: Optional[int]
  percentage: Optional[int]
  level: Optional[int]
  scale: Optional[int]
  charge_counter: Optional[int]
  energy: Optional[str]
  cycle: Optional[int]
class Phone(BaseModel):
    model: str
    android_version: str
    battery: Battery
    notifications: Optional[str]



@router.post("/send_heartbeat/")
async def heartsend_heartbeatbeat(session = Depends(get_db)):
  
  resp_battery_status = json.loads(subprocess.check_output(['termux-battery-status']).decode('utf-8'))

  #### GETTING DATA

  battery_formmated = Battery(**resp_battery_status)

  phone = Phone(
   model="x", #TEMPORARY
   android_version="x", #TEMPORARY
   battery=battery_formmated,
   notifications=None #TEMPORARY
  )
  
  #### RETURNING FOR DOKKA
    
  try:
    async with httpx.AsyncClient() as client: # o request. não aceita assíncrono, este sim
      
      resp = await client.post(f"http://{ip_dokka}/brain/heartbeat", 
                               json={"token_dokka": key, "phone_data": phone.model_dump()},
                               timeout=5.0)
      
    if resp.status_code == 200:
      return phone
    else:
      raise HTTPException(status_code=401, detail="ERRO ao enviar heartbeat.")
  except Exception as e:
    raise HTTPException(status_code=401, detail="ERRO ao enviar heartbeat.")
  

@router.post("/status/")
async def status(session = Depends(get_db)):
  
  return True

@router.post("/photo/")
async def photo(session = Depends(get_db)):
  
  return True

