# recetas.py 
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import get_db

router = APIRouter()

@router.post("/recetas/", response_model=schemas.RecetaBase)
def crear_receta(receta: schemas.RecetaBase, db: Session = Depends(get_db)):
    db_receta = models.Receta(**receta.dict())
    db.add(db_receta)
    db.commit()
    db.refresh(db_receta)
    return db_receta

@router.get("/recetas/{receta_id}", response_model=schemas.RecetaBase)
def get_receta(receta_id: int, db: Session = Depends(get_db)):
    db_receta = db.query(models.Receta).filter(models.Receta.id_receta == receta_id).first()
    if not db_receta:
        raise HTTPException(status_code=404, detail="Receta no encontrada")
    return db_receta 