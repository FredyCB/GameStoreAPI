from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from utils.database import Base

class Juego(Base):
    __tablename__ = "Juegos"

    id = Column(Integer, primary_key=True, index=True)
    nombre_juego = Column(String(200), nullable=False)

    # Relación 1:N con Inventario
    inventario_id = Column(Integer, ForeignKey("Inventario.id"), nullable=False)
