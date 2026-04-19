from typing import Annotated
import bcrypt
from fastapi import APIRouter, Body, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from sqlalchemy import select 
import jwt
from pydantic import BaseModel
from api.helpers.text_helper import verify_password

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


class Login(BaseModel):
    username: str
    password: str

@router.post("/login")
async def logs(req: Login, session: Session = Depends(get_db)):
    statement = select(User).where(User.username == req.username)
    user = session.execute(statement).scalars().first()

    if not user or not verify_password(req.password, user.password_hash):
        raise HTTPException(
            status_code=401, 
            detail="ERRO: Usuário ou senha incorretos."
        )

    return {
        "result": True,
        "message": f"Bem-vindo, {user.username}!",
        "user_id": user.id_usuario 
    }