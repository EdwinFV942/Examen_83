from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from datetime import date

from schemas import alumno_schema
from controllers import alumno_controller
from utils.security import get_current_user  # ✅ IMPORTANTE: Importamos la dependencia correcta

router = APIRouter(
    prefix="/students",
    tags=["Alumnos"]
)

# --- RUTAS PÚBLICAS ---
@router.get("/", response_model=List[alumno_schema.AlumnoResponse])
def get_alumnos(
    fecha_inicio: Optional[date] = Query(None, description="Formato YYYY-MM-DD"),
    fecha_fin: Optional[date] = Query(None, description="Formato YYYY-MM-DD")
):
    if fecha_inicio and fecha_fin:
        return alumno_controller.filtrar_por_fecha(fecha_inicio, fecha_fin)
    return alumno_controller.obtener_alumnos()

@router.get("/{id}", response_model=alumno_schema.AlumnoResponse)
def get_alumno(id: int):
    return alumno_controller.get_alumno(id)


# --- RUTAS PROTEGIDAS (Requieren Token) ---
@router.post("/", response_model=alumno_schema.AlumnoResponse)
def create_alumno(
    alumno_data: alumno_schema.AlumnoCreate, 
    current_user: str = Depends(get_current_user) # ✅ FastAPI extraerá el token de los Headers
):
    return alumno_controller.crear_alumno(alumno_data)

@router.put("/{id}", response_model=alumno_schema.AlumnoResponse)
def update_alumno(
    id: int, 
    alumno_data: alumno_schema.AlumnoUpdate, 
    current_user: str = Depends(get_current_user) # ✅ FastAPI extraerá el token de los Headers
):
    return alumno_controller.actualizar_alumno(id, alumno_data)

@router.delete("/{id}")
def delete_alumno(
    id: int, 
    current_user: str = Depends(get_current_user) # ✅ FastAPI extraerá el token de los Headers
):
    return alumno_controller.eliminar_alumno(id)