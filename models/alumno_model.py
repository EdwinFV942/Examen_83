from sqlalchemy import Column, Integer, String, Date
from db.database import Base
from datetime import date

class Alumno(Base):
    __tablename__ = "alumnos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    apellido_paterno = Column(String(100))
    apellido_materno = Column(String(100))
    matricula = Column(String(50), unique=True)
    correo = Column(String(100))
    password = Column(String(255))
    fecha_alta = Column(Date, default=date.today)