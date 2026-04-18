# services/auth_service.py

from db.database import SessionLocal
from models.alumno_model import Alumno
from passlib.context import CryptContext

# 🔐 Configuración bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# 🔑 Verificar password (IMPORTANTE limitar a 72 chars)
def verificar_password(password: str, hashed_password: str):
    try:
        return pwd_context.verify(password[:72], hashed_password)
    except Exception as e:
        print("💥 Error verificando password:", e)
        return False


# 🔐 Login
def login(matricula: str, password: str):
    db = SessionLocal()

    try:
        alumno = db.query(Alumno).filter(
            Alumno.matricula == matricula
        ).first()

        if not alumno:
            print("❌ Alumno no encontrado")
            return None

        print("Password ingresada:", password)
        print("Password BD:", alumno.password)

        # 🔍 Validar password correctamente
        if not verificar_password(password, alumno.password):
            print("❌ Password incorrecto")
            return None

        print("✅ Login correcto")
        return alumno

    finally:
        db.close()