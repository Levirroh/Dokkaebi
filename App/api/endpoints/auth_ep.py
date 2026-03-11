from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, HTTPException, Header
import jwt
from pydantic import BaseModel

from App.database.session import get_db
from App.models.user_model import User

from dotenv import load_dotenv
import os
key = os.getenv("DOKKA_KEY")
load_dotenv()


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

class Login(BaseModel):
    token_dokka: str # dokka id already inside dokka token



app = FastAPI()

@app.post("/login/")
async def logs(req: Annotated[Login | None, Body()], header: Annotated[str | None, Header()] = None, session = Depends(get_db)):
  try:
    login = jwt.decode(header, key, algorithms=["HS256"])
    
    password = login["password"]
    username = login["username"]
    
    user = session.select(User).where(User.username == login["username"] and User.usernamepassword == jwt.encode(login["password"], key, algorithm=["HS256"])).first()
    
    if(not user):
        raise HTTPException(status_code=404, detail="ERRO: Usuário não encontrado.")
        
    
  except jwt.exceptions.InvalidTokenError:
    raise HTTPException(status_code=401, detail="ERRO: Token Inválido ou Expirado.")

  return {"result": True}

