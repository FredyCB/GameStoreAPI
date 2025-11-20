from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Orden import OrdenCreate, OrdenResponse
from Controllers.Orden_controller import OrdenController

router = APIRouter()

@router.get("/", response_model=list[OrdenResponse])
def list_orders(db: Session = Depends(get_db)):
    return OrdenController.list_all(db)

@router.get("/{orden_id}", response_model=OrdenResponse)
def get_order(orden_id: int, db: Session = Depends(get_db)):
    o = OrdenController.get(db, orden_id)
    if not o:
        raise HTTPException(404, "Orden not found")
    return o

@router.post("/", response_model=OrdenResponse)
def create_order(payload: OrdenCreate, db: Session = Depends(get_db)):
    try:
        return OrdenController.create(db, payload)
    except Exception as e:
        raise HTTPException(400, str(e))


@router.delete("/{orden_id}", response_model=OrdenResponse)
def delete_order(orden_id: int, db: Session = Depends(get_db)):
    try:
        orden = OrdenController.delete(db, orden_id)
        if not orden:
            raise HTTPException(404, "Orden no encontrada")
        return orden
    except Exception as e:
        raise HTTPException(400, str(e))