from fastapi import APIRouter, FastAPI

from database.session import get_db


from dotenv import load_dotenv
import os
load_dotenv()
key = os.getenv("DOKKA_KEY")

router = APIRouter(
    prefix="/system",
    tags=["system"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)
