from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from database.base_class import Base

class Agent(Base):
    id_agente = Column(String, primary_key=True)
    nome_agente = Column(String)
    ip_local = Column(String)
    id_hardware = Column(String, unique=True)
    batery = Column(Integer)
    status_atual = Column(String) # Online, Offline, Alerta, Lockdown
    ultima_conexao = Column(DateTime)

class AgentConfig(Base):
    id_config = Column(Integer, primary_key=True)
    id_agente = Column(String, ForeignKey("agent.id_agente"))
    chave = Column(String)
    valor = Column(String)
    
class AgentSession(Base):
    __tablename__ = "agent_sessions"
    
    id_sessao = Column(String, primary_key=True) # UUID
    id_agente = Column(String, ForeignKey("agent.id_agente"))
    token_sessao = Column(String, unique=True, index=True)
    ip_origem = Column(String)
    user_agent_dispositivo = Column(String) # Ex: "Dokka-Android-12"
    criado_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime)
    ativa = Column(Boolean, default=True)