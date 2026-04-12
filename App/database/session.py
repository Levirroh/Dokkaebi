from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Padrão: mysql://usuario:senha@host:porta/nome_do_banco
SQLALCHEMY_DATABASE_URL = "mysql://root:root@localhost:3306/dokkaebi"

# No MySQL não precisamos do 'check_same_thread'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()