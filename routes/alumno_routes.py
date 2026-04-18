from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from schemas import alumno_schema
from controllers import alumno_controller
from utils.security import verify_token
from db.database import get_db # Asegúrate de tener esta dependencia en tu db/database.py

router = APIRouter(
    prefix="/students",
    tags=["Alumnos"]
)

# --- RUTAS PÚBLICAS ---
@router.get("/", response_model=List[alumno_schema.AlumnoResponse])
def get_alumnos(
    fecha_inicio: Optional[date] = Query(None, description="Formato YYYY-MM-DD"),
    fecha_fin: Optional[date] = Query(None, description="Formato YYYY-MM-DD"),
    db: Session = Depends(get_db)
):
    return alumno_controller.get_alumnos(db, fecha_inicio, fecha_fin)

@router.get("/{id}", response_model=alumno_schema.AlumnoResponse)
def get_alumno(id: int, db: Session = Depends(get_db)):
    return alumno_controller.get_alumno(db, id)


# --- RUTAS PROTEGIDAS (Requieren Token) ---
@router.post("/", response_model=alumno_schema.AlumnoResponse)
def create_alumno(
    alumno_data: alumno_schema.AlumnoCreate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token) # ← Protegido
):
    return alumno_controller.create_alumno(db, alumno_data)

@router.put("/{id}", response_model=alumno_schema.AlumnoResponse)
def update_alumno(
    id: int, 
    alumno_data: alumno_schema.AlumnoUpdate, 
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token) # ← Protegido
):
    return alumno_controller.update_alumno(db, id, alumno_data)

@router.delete("/{id}")
def delete_alumno(
    id: int, 
    db: Session = Depends(get_db),
    current_user: str = Depends(verify_token) # ← Protegido
):
    return alumno_controller.delete_alumno(db, id)