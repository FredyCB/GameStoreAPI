from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Orden import OrdenCreate, OrdenResponse
from Controllers.Orden_controller import OrdenController

router = APIRouter(prefix="/ordenes", tags=["Ordenes"])

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
    except ValueError as e:
        # errores por validación (cliente no existe, juego no existe, duplicados, etc)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # errores inesperados -> 500
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/{orden_id}")
def delete_order(orden_id: int, db: Session = Depends(get_db)):
    res = OrdenController.delete(db, orden_id)
    if not res:
        raise HTTPException(404, "Orden not found")
    return {"detail": "Orden eliminada correctamente"}
