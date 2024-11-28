# especialidades.py 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/especialidades/", response_model=schemas.EspecialidadBase)
def crear_especialidad(especialidad: schemas.EspecialidadBase, db: Session = Depends(get_db)):
    db_especialidad = models.Especialidad(**especialidad.dict())
    db.add(db_especialidad)
    db.commit()
    db.refresh(db_especialidad)
    return db_especialidad

@router.get("/especialidades/{especialidad_id}", response_model=schemas.EspecialidadBase)
def get_especialidad(especialidad_id: int, db: Session = Depends(get_db)):
    db_especialidad = db.query(models.Especialidad).filter(models.Especialidad.id_especialidad == especialidad_id).first()
    if not db_especialidad:
        raise HTTPException(status_code=404, detail="Especialidad no encontrada")
    return db_especialidad 