# controllers/auth_controller.py
from fastapi import HTTPException
from schemas.alumno_schema import AlumnoLogin
from services import auth_service
from utils.security import generate_token as crear_token

def login(user: AlumnoLogin):
    alumno = auth_service.login(user.matricula, user.password)
    print(f"Alumno encontrado: {alumno}")  # Debug: Verificar si se encuentra el alumno
    if not alumno:
        raise HTTPException(
            status_code=401,
            detail="Matrícula o contraseña incorrecta"
        )

    token = crear_token({
        "sub": alumno.matricula,
        "nombre": alumno.nombre
    })

    return {
        "mensaje": "Login exitoso",
        "access_token": token,
        "token_type": "bearer",
        "usuario": {
            "matricula": alumno.matricula,
            "nombre": alumno.nombre
        }
    }