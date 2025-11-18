from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from utils.database import Base

class Orden(Base):
    __tablename__ = "Ordenes"

    id = Column(Integer, primary_key=True, index=True)

    cliente_id = Column(Integer, ForeignKey("Clientes.id"), nullable=False)
    cliente_nombre = Column(String(120), nullable=False)   # <-- CAMPO FALTANTE

    fecha_orden = Column(DateTime, server_default=func.now(), nullable=False)

    total = Column(DECIMAL(10,2), nullable=False, default=0)
    estado = Column(String(20), default="Pendiente")
