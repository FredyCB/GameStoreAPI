from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db

from schemas.Inventario import (
    InventarioCreate,
    InventarioResponse,
    InventarioUpdateStock,
    InventarioUpdatePrecio
)

from Controllers.Inventario_controller import InventarioController

router = APIRouter()


@router.get("/", response_model=list[InventarioResponse])
def list_inv(db: Session = Depends(get_db)):
    return InventarioController.list_all(db)


@router.put("/{inv_id}", response_model=InventarioResponse)
def update_stock(inv_id: int, payload: InventarioUpdateStock, db: Session = Depends(get_db)):
    inv = InventarioController.update_stock(db, inv_id, payload)
    if not inv:
        raise HTTPException(404, "Inventario not found")
    return inv


@router.put("/{inv_id}/precio", response_model=InventarioResponse)
def update_precio(inv_id: int, payload: InventarioUpdatePrecio, db: Session = Depends(get_db)):
    inv = InventarioController.update_precio(db, inv_id, payload)
    if not inv:
        raise HTTPException(404, "Inventario not found")
    return inv
