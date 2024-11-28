# expedientes.py 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/expedientes/", response_model=schemas.ExpedienteBase)
def crear_expediente(expediente: schemas.ExpedienteBase, db: Session = Depends(get_db)):
    db_expediente = models.Expediente(**expediente.dict())
    db.add(db_expediente)
    db.commit()
    db.refresh(db_expediente)
    return db_expediente

@router.get("/expedientes/{expediente_id}", response_model=schemas.ExpedienteBase)
def get_expediente(expediente_id: int, db: Session = Depends(get_db)):
    db_expediente = db.query(models.Expediente).filter(models.Expediente.id_expediente == expediente_id).first()
    if not db_expediente:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    return db_expediente 