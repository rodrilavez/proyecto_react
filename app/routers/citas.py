# citas.py 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/citas/", response_model=schemas.CitaBase)
def crear_cita(cita: schemas.CitaBase, db: Session = Depends(get_db)):
    db_cita = models.Cita(**cita.dict())
    db.add(db_cita)
    db.commit()
    db.refresh(db_cita)
    return db_cita

@router.get("/citas/{cita_id}", response_model=schemas.CitaBase)
def get_cita(cita_id: int, db: Session = Depends(get_db)):
    db_cita = db.query(models.Cita).filter(models.Cita.id_cita == cita_id).first()
    if not db_cita:
        raise HTTPException(status_code=404, detail="Cita no encontrada")
    return db_cita 