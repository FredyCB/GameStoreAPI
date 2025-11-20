from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL, String
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from utils.database import Base

class Orden(Base):
    __tablename__ = "Ordenes"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("Clientes.id"), nullable=False)
    cliente_nombre = Column(String(120), nullable=False)  # agregado para almacenar nombre cliente
    fecha_orden = Column(DateTime, server_default=func.now(), nullable=False)
    total = Column(DECIMAL(12,2), default=0, nullable=False)
    estado = Column(String(50), default="Pendiente", nullable=False)

    # relación con detalle de la Orden
    detalles = relationship("DetalleOrden", back_populates="orden", cascade="all, delete-orphan")

