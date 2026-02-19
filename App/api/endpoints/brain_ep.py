from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, HTTPException, Header
import jwt
from pydantic import BaseModel

from App.database.session import get_db
from App.models.agent_model import Agent
from App.models.system_model import Log

key = "#acegik!*"

router = APIRouter(
    prefix="/data",
    tags=["data"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

class Check(BaseModel):
    token_dokka: str # dokka id already inside dokka token


app = FastAPI()

@app.post("/heartbeat/")
async def heartbeat(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  try:
    agent = jwt.decode(header, key, algorithms=["HS256"])
    
    db_agent = session.select(Agent).where(Agent.id == agent["id"]).first()
    
    if(db_agent != None):
        db_agent.batery = req.batery
        db_agent.status = "ONLINE"
        db_agent.ultima_conexao = datetime.now()
        
        session.commit()
    else:
      raise HTTPException(status_code=404, detail="ERRO: Agente não encontrado.")
    
  except jwt.exceptions.InvalidTokenError:
    raise HTTPException(status_code=401, detail="ERRO: Token Inválido ou Expirado.")

  return {"message": "Dokkaebi online", "agent": agent}


@app.post("/logs/")
async def logs(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  try:
    jwt.decode(header, key, algorithms=["HS256"])
    
    logs = session.select(Log).all()
    
    return logs
    
  except jwt.exceptions.InvalidTokenError:
    raise HTTPException(status_code=401, detail="ERRO: Token Inválido ou Expirado.")


@app.post("/agents/:id")
async def get_agent(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  return True

@app.post("/notifications/")
async def notifications(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  return True