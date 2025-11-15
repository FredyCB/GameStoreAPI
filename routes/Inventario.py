from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils.database import get_db
from schemas.Inventario import InventarioCreate, InventarioResponse
from Controllers.Inventario_controller import InventarioController

router = APIRouter()

@router.get("/", response_model=list[InventarioResponse])
def list_inv(db: Session = Depends(get_db)):
    return InventarioController.list_all(db)

@router.get("/{inv_id}", response_model=InventarioResponse)
def get_inv(inv_id: int, db: Session = Depends(get_db)):
    inv = InventarioController.get(db, inv_id)
    if not inv:
        raise HTTPException(404, "Inventario not found")
    return inv

@router.post("/", response_model=InventarioResponse)
def create_inv(payload: InventarioCreate, db: Session = Depends(get_db)):
    return InventarioController.create(db, payload)

@router.put("/{inv_id}", response_model=InventarioResponse)
def update_inv(inv_id: int, payload: InventarioCreate, db: Session = Depends(get_db)):
    inv = InventarioController.update(db, inv_id, payload)
    if not inv:
        raise HTTPException(404, "Inventario not found")
    return inv
