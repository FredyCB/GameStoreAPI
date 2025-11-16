from sqlalchemy.orm import Session
from models.Juego import Juego
from schemas.Juego import JuegoCreate, JuegoUpdate

class JuegoController:

    @staticmethod
    def list_all(db: Session):
        return db.query(Juego).all()

    @staticmethod
    def get(db: Session, juego_id: int):
        return db.query(Juego).filter(Juego.id == juego_id).first()

    @staticmethod
    def create(db: Session, payload: JuegoCreate):
        obj = Juego(
            nombre_juego=payload.nombre_juego,
            inventario_id=payload.inventario_id
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update(db: Session, juego_id: int, payload: JuegoUpdate):
        obj = db.query(Juego).filter(Juego.id == juego_id).first()
        if not obj:
            return None

        if payload.nombre_juego is not None:
            obj.nombre_juego = payload.nombre_juego
        
        if payload.inventario_id is not None:
            obj.inventario_id = payload.inventario_id

        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def delete(db: Session, juego_id: int):
        obj = db.query(Juego).filter(Juego.id == juego_id).first()
        if not obj:
            return None

        db.delete(obj)
        db.commit()
        return obj
