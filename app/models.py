# models.py 
from sqlalchemy import Column, Integer, String, Enum, Date, Text, ForeignKey, Time, TIMESTAMP
from sqlalchemy.orm import relationship
from app.database import Base


class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    rol = Column(Enum("paciente", "doctor"), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    cedula_profesional = Column(String(50), nullable=True)
    especialidad = Column(String(100), nullable=True)
    fecha_registro = Column(TIMESTAMP)

class Cita(Base):
    __tablename__ = "citas"
    id_cita = Column(Integer, primary_key=True, index=True)
    id_paciente = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    id_doctor = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha_cita = Column(Date, nullable=False)
    hora_cita = Column(Time, nullable=False)
    estado = Column(Enum("pendiente", "confirmada"), default="pendiente")
    paciente = relationship("Usuario", foreign_keys=[id_paciente])
    doctor = relationship("Usuario", foreign_keys=[id_doctor])

class Expediente(Base):
    __tablename__ = "expedientes"
    id_expediente = Column(Integer, primary_key=True, index=True)
    id_paciente = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    anotaciones = Column(Text, nullable=True)
    fecha_cita = Column(TIMESTAMP, nullable=False)

class Receta(Base):
    __tablename__ = "recetas"
    id_receta = Column(Integer, primary_key=True, index=True)
    id_cita = Column(Integer, ForeignKey("citas.id_cita"), nullable=False)
    anotaciones = Column(Text, nullable=False)
    medicamentos = Column(Text, nullable=False)

class Especialidad(Base):
    __tablename__ = "especialidades"
    id_especialidad = Column(Integer, primary_key=True, index=True)
    nombre_especialidad = Column(String(100), nullable=False)
