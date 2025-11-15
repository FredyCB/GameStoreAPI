from sqlalchemy.orm import Session
from decimal import Decimal
from models.Inventario import Inventario
from schemas.Inventario import InventarioCreate, InventarioUpdateStock, InventarioUpdatePrecio
from typing import Any, Mapping

class InventarioController:

    @staticmethod
    def list_all(db: Session):
        return db.query(Inventario).all()

    @staticmethod
    def get(db: Session, inv_id: int):
        return db.query(Inventario).filter(Inventario.id == inv_id).first()

    @staticmethod
    def create(db: Session, data: InventarioCreate):
        obj = Inventario(
            nombre=data.nombre,
            precio=data.precio,
            stock=data.stock if data.stock is not None else 0,
            ubicacion=data.ubicacion
        )
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update_stock(db: Session, inv_id: int, data: Any):
        """
        data puede ser un Pydantic model o un dict. Normalizamos y aplicamos solo si hay valor.
        """
        obj = db.query(Inventario).filter(Inventario.id == inv_id).first()
        if not obj:
            return None

        # Normalizar payload a dict
        if hasattr(data, "dict"):
            payload = data.dict()
        elif isinstance(data, Mapping):
            payload = dict(data)
        else:
            # si llega otro tipo, intentar convertir vía __dict__
            payload = getattr(data, "__dict__", {}) or {}

        # Tomar el valor solo si viene presente (no sobrescribir con None)
        if "stock" in payload and payload["stock"] is not None:
            try:
                obj.stock = payload["stock"]
            except (TypeError, ValueError):
                # si la conversión falla, no aplicamos el cambio y podemos optar por raise o ignorar.
                raise ValueError("El campo 'stock' debe ser un entero válido")

        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def update_precio(db: Session, inv_id: int, data: Any):
        """
        Actualiza precio. data puede ser Pydantic model o dict.
        """
        obj = db.query(Inventario).filter(Inventario.id == inv_id).first()
        if not obj:
            return None

        # Normalizar payload a dict
        if hasattr(data, "dict"):
            payload = data.dict()
        elif isinstance(data, Mapping):
            payload = dict(data)
        else:
            payload = getattr(data, "__dict__", {}) or {}
        if "precio" in payload and payload["precio"] is not None:
            try:
                setattr(obj, "precio", float(payload["precio"]))
            except (TypeError, ValueError):
                raise ValueError("El campo 'precio' debe ser un número válido")
        db.commit()
        db.refresh(obj)
        return obj