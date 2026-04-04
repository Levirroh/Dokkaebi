from fastapi import APIRouter, Depends, FastAPI

from database.session import get_db
from models.agent_model import Agent


from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("DOKKA_KEY")

router = APIRouter(
    prefix="/master",
    tags=["master"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/dashboard/")
async def dashboard(session = Depends(get_db)):

  result = session.query(Agent).all()
  
  return result


