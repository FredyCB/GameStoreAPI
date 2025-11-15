from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
from utils.database import Base

class DetalleOrden(Base):
    __tablename__ = "DetalleOrden"
    id = Column(Integer, primary_key=True, index=True)
    orden_id = Column(Integer, ForeignKey("Ordenes.id"), nullable=False)
    inventario_id = Column(Integer, ForeignKey("Inventario.id"), nullable=False)  # referencia al inventario
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(DECIMAL(10,2))
    orden = relationship("Orden", back_populates="detalles")
    # relación con inventario si la necesitas:
    # inventario = relationship("Inventario")
