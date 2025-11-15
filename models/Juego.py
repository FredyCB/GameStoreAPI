from sqlalchemy import Column, Integer, String, DECIMAL, Text, ForeignKey
from sqlalchemy.orm import relationship
from utils.database import Base

class Juego(Base):
    __tablename__ = "Juegos"
    id = Column(Integer, primary_key=True, index=True)
    inventario_id = Column(Integer, ForeignKey("Inventario.id"), nullable=False)  # FK al inventario
    titulo = Column(String(250), nullable=False)
    descripcion = Column(Text)
    precio = Column(DECIMAL(10,2))
