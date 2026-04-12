from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database.base_class import Base

class User(Base):
    id_usuario = Column(String(36), primary_key=True)
    username = Column(String(100), unique=True, index=True)
    password_hash = Column(String(255))
    permissoes = Column(String(2), default="00") # [Ver][Executar]
    digital_cadastrada = Column(Boolean, default=False)

class Biometria(Base):
    id_biometria = Column(Integer, primary_key=True)
    id_usuario = Column(String(36), ForeignKey("user.id_usuario"))
    hash_biometrico = Column(String(255))