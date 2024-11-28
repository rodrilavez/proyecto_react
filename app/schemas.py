# schemas.py 

from pydantic import BaseModel
from typing import Optional
from datetime import date, time

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    fecha_nacimiento: date
    rol: str

class UsuarioCreate(UsuarioBase):
    password: str

class CitaBase(BaseModel):
    id_paciente: int
    id_doctor: int
    fecha_cita: date
    hora_cita: time

class ExpedienteBase(BaseModel):
    id_paciente: int
    anotaciones: str
    fecha_cita: date

class RecetaBase(BaseModel):
    id_cita: int
    anotaciones: str
    medicamentos: str

class EspecialidadBase(BaseModel):
    nombre_especialidad: str
