from sqlalchemy.orm import Session
from models.Clientes import Cliente
from schemas.Clientes import ClienteCreate

class ClienteController:
    @staticmethod
    def list_all(db: Session):
        return db.query(Cliente).all()

    @staticmethod
    def get(db: Session, cliente_id: int):
        return db.query(Cliente).filter(Cliente.id == cliente_id).first()

    @staticmethod
    def create(db: Session, data: ClienteCreate):
        obj = Cliente(nombre=data.nombre, email=data.email, telefono=data.telefono)
        db.add(obj); db.commit(); db.refresh(obj)
        return obj

    @staticmethod
    def delete(db: Session, cliente_id: int):
        obj = db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if not obj: return None
        db.delete(obj); db.commit()
        return obj
