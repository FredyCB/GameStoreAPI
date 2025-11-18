from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError

from models.Cliente import Clientes
from models.Inventario import Inventario
from models.Orden import Orden
from models.Detalle_Orden import DetalleOrden


class OrdenController:

    @staticmethod
    def list_all(db: Session):
        return db.query(Orden).all()

    @staticmethod
    def get(db: Session, orden_id: int):
        return db.query(Orden).filter(Orden.id == orden_id).first()

    @staticmethod
    def create(db: Session, data):
        # VALIDAR CLIENTE
        cliente = db.query(Clientes).filter(Clientes.id == data.cliente_id).first()
        if not cliente:
            raise ValueError("Cliente no encontrado")

        # Crear encabezado de orden
        orden = Orden(
            cliente_id=cliente.id,
            cliente_nombre=cliente.nombre,
            estado="Pendiente",
            total=0
        )

        try:
            db.add(orden)
            db.commit()
            db.refresh(orden)
        except:
            db.rollback()
            raise

        total = 0

        # AGREGAR LOS JUEGOS
        for item in data.juegos:
            inv = db.query(Inventario).filter(Inventario.nombre == item.nombre_juego).first()
            if not inv:
                raise ValueError(f"Juego '{item.nombre_juego}' no existe en inventario")

            detalle = DetalleOrden(
                orden_id=orden.id,
                inventario_id=inv.id,
                nombre_inventario=inv.nombre,
                cantidad=item.cantidad,
                precio_unitario=inv.precio
            )

            total += inv.precio * item.cantidad

            db.add(detalle)

        # ACTUALIZAR TOTAL FINAL
        try:
            orden.total = total
            db.commit()
        except SQLAlchemyError:
            db.rollback()
            raise

        db.refresh(orden)
        return orden

    @staticmethod
    def delete(db: Session, orden_id: int):
        orden = db.query(Orden).filter(Orden.id == orden_id).first()
        if not orden:
            return None

        try:
            db.delete(orden)
            db.commit()
        except:
            db.rollback()
            raise

        return orden
