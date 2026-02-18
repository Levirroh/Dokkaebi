from typing import Annotated
from fastapi import APIRouter, Body, Depends, FastAPI, Header
from pydantic import BaseModel

from App.database.session import get_db

key = "#ifoieibnvienv"

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)


app = FastAPI()

