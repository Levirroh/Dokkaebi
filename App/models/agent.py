from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from database.base_class import Base

class Agent(Base):
    id_agente = Column(String, primary_key=True)
    nome_agente = Column(String)
    ip_local = Column(String)
    id_hardware = Column(String, unique=True)
    status_atual = Column(String) # Online, Offline, Alerta, Lockdown
    ultima_conexao = Column(DateTime)

class AgentConfig(Base):
    id_config = Column(Integer, primary_key=True)
    id_agente = Column(String, ForeignKey("agent.id_agente"))
    chave = Column(String)
    valor = Column(String)