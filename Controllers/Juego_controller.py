from sqlalchemy.orm import Session
from models.Juego import Juego
from schemas.Juego import JuegoCreate

class JuegoController:
    @staticmethod
    def list_by_inventario(db: Session, inventario_id: int):
        return db.query(Juego).filter(Juego.inventario_id == inventario_id).all()

    @staticmethod
    def get(db: Session, juego_id: int):
        return db.query(Juego).filter(Juego.id == juego_id).first()

    @staticmethod
    def create(db: Session, data: JuegoCreate):
        obj = Juego(inventario_id=data.inventario_id, titulo=data.titulo, descripcion=data.descripcion, precio=data.precio)
        db.add(obj); db.commit(); db.refresh(obj)
        return obj

    @staticmethod
    def delete(db: Session, juego_id: int):
        obj = db.query(Juego).filter(Juego.id == juego_id).first()
        if not obj: return None
        db.delete(obj); db.commit()
        return obj

