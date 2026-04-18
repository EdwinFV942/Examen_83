from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date

class AlumnoCreate(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    matricula: str
    correo: EmailStr
    password: str


class Alumno(BaseModel):
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    matricula: str
    correo: EmailStr
    fecha_alta: date

    class Config:
        orm_mode = True

class AlumnoLogin(BaseModel):
    matricula: str
    password: str


class AlumnoResponse(BaseModel):
    id: int
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    matricula: str
    correo: str
    fecha_alta: date

    # ✅ Pydantic V2 (IMPORTANTE)
    model_config = ConfigDict(from_attributes=True)

class AlumnoUpdate(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    matricula: str
    correo: str
    password: str