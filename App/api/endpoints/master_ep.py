from fastapi import APIRouter, Depends, FastAPI

from App.database.session import get_db
from App.models.agent_model import Agent


from dotenv import load_dotenv
import os
key = os.getenv("DOKKA_KEY")
load_dotenv()

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


