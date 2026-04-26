import select
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from api.router import api_router
from database.session import get_db
from models.user_model import User

# Importe aqui o seu get_db e seus Models (ajuste o caminho se necessário)
# from database import get_db
# from models import User

app = FastAPI(title="Dokkaebi Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/ping")
async def ping():
    return {"status": "online", "message": "Dokkaebi System Active"}

@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    statement = select(User).limit(1)
    result = db.execute(statement).scalars().first()
    return {"message": "Conexão com banco pronta para implementar"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)