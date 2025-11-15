from sqlalchemy.orm import Session
from sqlalchemy import text
from models.Orden import Orden
from models.Detalle_Orden import DetalleOrden
from models.Inventario import Inventario
from schemas.Orden import OrdenCreate
from datetime import datetime

class OrdenController:
    @staticmethod
    def get(db: Session, orden_id: int):
        return db.query(Orden).filter(Orden.id == orden_id).first()

    @staticmethod
    def list_all(db: Session):
        return db.query(Orden).all()
    @staticmethod
    def create(db: Session, data: OrdenCreate):
        # validate cliente exists
        cliente_exists = db.execute(text(f"SELECT 1 FROM Clientes WHERE id={data.cliente_id}")).fetchone()
        if not cliente_exists:
            raise Exception("Cliente not found")
            raise Exception("Cliente not found")

        orden = Orden(cliente_id=data.cliente_id, fecha_orden=datetime.now(), total=data.total or 0)
        db.add(orden); db.commit(); db.refresh(orden)

        # process detalles: deduct stock from Inventario when necessary?
        for d in data.detalles:
            inv = db.query(Inventario).filter(Inventario.id == d.inventario_id).first()
            if not inv:
                raise Exception(f"Inventario {d.inventario_id} not found")
            # Optionally check stock on inv (if you keep stock elsewhere)
            detalle = DetalleOrden(orden_id=orden.id, inventario_id=d.inventario_id,
                                    cantidad=d.cantidad, precio_unitario=d.precio_unitario)
            db.add(detalle)
        db.commit()
        db.refresh(orden)
        return orden
