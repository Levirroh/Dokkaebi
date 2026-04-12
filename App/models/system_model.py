from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Text
from datetime import datetime
from database.base_class import Base

class Command(Base):
    id_comando = Column(Integer, primary_key=True)
    id_agente = Column(String(36), ForeignKey("agent.id_agente"))
    tipo = Column(String(50))  # FOTO, LOCKDOWN, AUDIO
    status = Column(String(50), default="Pendente")  # Pendente, Executado, Falha
    timestamp = Column(DateTime, default=datetime.utcnow)

class Log(Base):
    id_log = Column(Integer, primary_key=True)
    id_agente = Column(String(36), ForeignKey("agent.id_agente"), nullable=True)
    evento = Column(String(100))
    timestamp = Column(DateTime, default=datetime.utcnow)
    
class Notification(Base):
    id_notificacao = Column(Integer, primary_key=True)
    id_agente = Column(String(36), ForeignKey("agent.id_agente"), nullable=True)
    titulo = Column(String(100))
    mensagem = Column(Text)
    lida = Column(Boolean, default=False)
    prioridade = Column(String(50), default="Baixa") # Baixa, Média, Crítica
    timestamp = Column(DateTime, default=datetime.now)

class GlobalConfig(Base):
    # Para configurações como 'modo_lockdown_ativo'
    chave = Column(String(50), primary_key=True)
    valor = Column(String(255))
    
    