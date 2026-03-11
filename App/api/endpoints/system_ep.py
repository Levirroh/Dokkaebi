from fastapi import APIRouter, FastAPI

from App.database.session import get_db


from dotenv import load_dotenv
import os
key = os.getenv("DOKKA_KEY")
load_dotenv()

router = APIRouter(
    prefix="/system",
    tags=["system"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


app = FastAPI()

