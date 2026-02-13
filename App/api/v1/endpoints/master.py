from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, HTTPException, Header
from pydantic import BaseModel
import jwt

from App.database.session import get_db
from App.models.agent import Agent

key = "#LMAZpoqiwe098123"

router = APIRouter(
    prefix="/master",
    tags=["master"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

app = FastAPI()

@app.get("/dashboard/")
async def dashboard(session = Depends(get_db)):

  result = session.query(Agent).all()
  
  return result


