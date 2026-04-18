from fastapi import HTTPException

from schemas.alumno_schema import AlumnoCreate
from services import alumno_service


def crear_alumno(alumno: AlumnoCreate):
    return alumno_service.crear(alumno)

def obtener_alumnos():
    return alumno_service.obtener()

def actualizar_alumno(id, alumno):
    result = alumno_service.actualizar(id, alumno)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Alumno no encontrado"
        )

    return result

def eliminar_alumno(id):
    result = alumno_service.eliminar(id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Alumno no encontrado"
        )

    return {"mensaje": "Alumno eliminado correctamente"}

def filtrar_por_fecha(inicio, fin):
    if inicio > fin:
        raise HTTPException(
            status_code=400,
            detail="La fecha inicio no puede ser mayor a la fecha fin"
        )

    return alumno_service.filtrar(inicio, fin)

def get_alumno(id):
    result = alumno_service.obtener_por_id(id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Alumno no encontrado"
        )

    return result