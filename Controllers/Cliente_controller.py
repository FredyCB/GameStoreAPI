from sqlalchemy.orm import Session
from models.Cliente import Clientes
from schemas.Clientes import ClienteCreate

class ClienteController:
    @staticmethod
    def list_all(db: Session):
        return db.query(Clientes).all()

    @staticmethod
    def get(db: Session, cliente_id: int):
        return db.query(Clientes).filter(Clientes.id == cliente_id).first()
    @staticmethod
    def create(db: Session, data: ClienteCreate):
        obj = Clientes(nombre=data.nombre, email=data.email, telefono=data.telefono)
        db.add(obj); db.commit(); db.refresh(obj)
        return obj

