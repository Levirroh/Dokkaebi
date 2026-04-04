from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from sqlalchemy import select 
import jwt
from pydantic import BaseModel
from passlib.context import CryptContext


from database.session import get_db
from models.user_model import User

from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("DOKKA_KEY")

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Login(BaseModel):
    username: str
    password: str

@router.post("/login")
async def logs(req: Login, session: Session = Depends(get_db)):
  statement = select(User).where(User.username == req.username)

  # provisório para teste, depois remover
  if(req.username == "admin" and req.password == "admin"):
    return {
      "result": True,
      "message": "Bem-vindo, admin!",
    }

  user = session.execute(statement).scalars().first()
  
  if not user or not pwd_context.verify(req.password, user.password_hash):
      raise HTTPException(status_code=401, detail="ERRO: Usuário ou senha incorretos.")
    
  return {
      "result": True,
      "message": f"Bem-vindo, {user.username}!",
      "user_id": user.id 
  }