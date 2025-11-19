from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Clientes import ClienteCreate, ClienteResponse
from Controllers.Cliente_controller import ClienteController

router = APIRouter()

@router.get("/", response_model=list[ClienteResponse])
def list_clients(db: Session = Depends(get_db)):
    return ClienteController.list_all(db)

@router.get("/{cliente_id}", response_model=ClienteResponse)
def get_client(cliente_id: int, db: Session = Depends(get_db)):
    c = ClienteController.get(db, cliente_id)
    if not c:
        raise HTTPException(404, "Cliente not found")
    return c

@router.post("/", response_model=ClienteResponse)
def create_client(payload: ClienteCreate, db: Session = Depends(get_db)):
    return ClienteController.create(db, payload)

