import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

load_dotenv()

engine = None
SessionLocal = None
CURRENT_DATABASE_URL = None


def configure_database(database_url: str = None):
    global engine
    global SessionLocal
    global CURRENT_DATABASE_URL

    database_url = database_url or os.getenv("DATABASE_URL_LOCAL")

    if not database_url:
        raise ValueError("DATABASE_URL não encontrada.")

    CURRENT_DATABASE_URL = database_url

    engine = create_engine(database_url)

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )

    return SessionLocal


def get_session():
    global SessionLocal

    if SessionLocal is None:
        configure_database()

    return SessionLocal()


def get_db():
    db = get_session()

    try:
        yield db
    finally:
        db.close()


def test_connection():
    db = get_session()

    try:
        db.execute(text("SELECT 1"))
        return True

    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return False

    finally:
        db.close()