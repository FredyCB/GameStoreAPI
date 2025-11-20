from sqlalchemy import Column, Integer, ForeignKey, DECIMAL, String
from sqlalchemy.orm import relationship
from utils.database import Base

class DetalleOrden(Base):
    __tablename__ = "Detalle_Orden"

    id = Column(Integer, primary_key=True, index=True)
    orden_id = Column(Integer, ForeignKey("Ordenes.id", ondelete="CASCADE"), nullable=False)
    inventario_id = Column(Integer, ForeignKey("Inventario.id"), nullable=False)

    nombre_inventario = Column(String(200), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(DECIMAL(10, 2), nullable=False)

    # Relaciones con Inventario y Orden
    orden = relationship("Orden", back_populates="detalles")
    inventario = relationship("Inventario")
