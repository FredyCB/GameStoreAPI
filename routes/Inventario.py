#routes/Inventario.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db

from Controllers.Inventario_controller import InventarioController
from schemas.Inventario import InventarioCreate, InventarioUpdate, InventarioResponse

# SIN prefix aquí
router = APIRouter(tags=["Inventarios"])

@router.get("/", response_model=list[InventarioResponse])
def list_all(db: Session = Depends(get_db)):
    return InventarioController.list_all(db)

@router.post("/", response_model=InventarioResponse)
def create(payload: InventarioCreate, db: Session = Depends(get_db)):
    return InventarioController.create(db, payload)

@router.get("/{inv_id}", response_model=InventarioResponse)
def get(inv_id: int, db: Session = Depends(get_db)):
    obj = InventarioController.get(db, inv_id)
    if not obj:
        raise HTTPException(404, "Inventario no encontrado")
    return obj

@router.put("/{inv_id}", response_model=InventarioResponse)
def update(inv_id: int, payload: InventarioUpdate, db: Session = Depends(get_db)):
    return InventarioController.update(db, inv_id, payload)

@router.delete("/{inv_id}", response_model=InventarioResponse)
def delete(inv_id: int, db: Session = Depends(get_db)):
    return InventarioController.delete(db, inv_id)