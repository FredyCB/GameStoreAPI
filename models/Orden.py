from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from utils.database import Base

class Orden(Base):
    __tablename__ = "Ordenes"
    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("Clientes.id"), nullable=False)
    fecha_orden = Column(DateTime, server_default=func.now())
    total = Column(DECIMAL(12,2), default=0)
    estado = Column(String(50), default="PENDIENTE")

