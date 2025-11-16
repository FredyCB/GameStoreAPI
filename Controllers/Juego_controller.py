from sqlalchemy.orm import Session
from models.Juego import Juego
from schemas.Juego import JuegoCreate
from models.Inventario import Inventario  # Para registrar inventario automáticamente
from typing import Any, cast

class JuegoController:

    @staticmethod
    def list_all(db: Session):
        return db.query(Juego).all()

    @staticmethod
    def get(db: Session, juego_id: int):
        return db.query(Juego).filter(Juego.inventario_id == juego_id).first()

    @staticmethod
    def create(db: Session, data: JuegoCreate):
        # Crear registro en Inventario primero
        inventario = Inventario(nombre=data.nombre, precio=float(data.precio))
        db.add(inventario)
        db.commit()
        db.refresh(inventario)

        # Crear juego vinculado al inventario
        juego = Juego(
            inventario_id=inventario.id,
            nombre=data.nombre,
            precio=float(data.precio)
        )
        db.add(juego)
        db.commit()
        db.refresh(juego)
        return juego

    @staticmethod
    def update(db: Session, juego_id: int, data: JuegoCreate):
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if not juego:
            return None
        # Actualizar datos en inventario también
        inv = db.query(Inventario).filter(Inventario.id == juego.inventario_id).first()
        if inv:
            inv_any = cast(Any, inv)
            inv_any.nombre = data.nombre
            inv_any.precio = float(data.precio)

        juego_any = cast(Any, juego)
        juego_any.nombre = data.nombre
        juego_any.precio = float(data.precio)
        db.commit()
        db.refresh(juego)
        return juego

    @staticmethod
    def delete(db: Session, juego_id: int):
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if not juego:
            return None

        # También eliminar inventario vinculado
        inv = db.query(Inventario).filter(Inventario.id == juego.inventario_id).first()
        if inv:
            db.delete(inv)
        db.delete(juego)
        db.commit()
        return juego
