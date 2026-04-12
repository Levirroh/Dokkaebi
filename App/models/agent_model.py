from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from database.base_class import Base

class Agent(Base):
    id_agente = Column(String(36), primary_key=True)
    nome_agente = Column(String(100))
    ip_local = Column(String(45))
    id_hardware = Column(String(36), unique=True)
    batery = Column(Integer)
    status_atual = Column(String(50)) # Online, Offline, Alerta, Lockdown
    ultima_conexao = Column(DateTime)

class AgentConfig(Base):
    id_config = Column(Integer, primary_key=True)
    id_agente = Column(String(36), ForeignKey("agent.id_agente"))
    chave = Column(String(100))
    valor = Column(String(255))
    
class AgentSession(Base):
    __tablename__ = "agent_sessions"
    
    id_sessao = Column(String(36), primary_key=True) # UUID
    id_agente = Column(String(36), ForeignKey("agent.id_agente"))
    token_sessao = Column(String(255), unique=True, index=True)
    ip_origem = Column(String(45))
    user_agent_dispositivo = Column(String(100)) # Ex: "Dokka-Android-12"
    criado_em = Column(DateTime, default=datetime.utcnow)
    expira_em = Column(DateTime)
    ativa = Column(Boolean, default=True)