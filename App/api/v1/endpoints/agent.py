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

@app.post("/heartbeat/")
async def heartbeat(req: Annotated[Check | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  try:
    agent = jwt.decode(header, key, algorithms=["HS256"])
    
    db_agent = session.query(Agent).filter(Agent.id == agent.get("id")).first()
    
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



@app.get("/dashboard/")
async def dashboard(session = Depends(get_db)):

  result = session.query(Agent).all()
  
  for agent in result:
    status = try_connection(agent, session)

    if(status == "OFFLINE"):
      agent.status ="OFFLINE"

  return result

async def try_connection(agent, session):
  # Aqui você usaria uma biblioteca como 'httpx' ou 'subprocess' para dar um ping
  # Estude a biblioteca 'httpx' para fazer requisições assíncronas
  
  result = "ONLINE" #placeholder
  
    
  return result