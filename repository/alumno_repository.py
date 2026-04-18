from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.alumno_model import Alumno
from db.database import SessionLocal
from datetime import datetime
from utils.security import hash_password


def guardar(alumno):
    db: Session = SessionLocal()

    try:
        # 🔍 Validar matrícula duplicada
        existe = db.query(Alumno).filter(Alumno.matricula == alumno.matricula).first()
        if existe:
            return None

        nuevo = Alumno(
            nombre=alumno.nombre,
            apellido_paterno=alumno.apellido_paterno,
            apellido_materno=alumno.apellido_materno,
            matricula=alumno.matricula,
            correo=alumno.correo,
            password=hash_password(alumno.password),
            fecha_alta=datetime.now().date()
        )

        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)

        return nuevo

    except IntegrityError:
        db.rollback()
        return None

    finally:
        db.close()


def obtener_todos():
    db: Session = SessionLocal()

    try:
        return db.query(Alumno).all()

    finally:
        db.close()


def obtener_por_id(id):
    db: Session = SessionLocal()

    try:
        return db.query(Alumno).filter(Alumno.id == id).first()

    finally:
        db.close()


def actualizar(id, alumno):
    db: Session = SessionLocal()

    try:
        alumno_db = db.query(Alumno).filter(Alumno.id == id).first()

        if not alumno_db:
            return None

        alumno_db.nombre = alumno.nombre
        alumno_db.apellido_paterno = alumno.apellido_paterno
        alumno_db.apellido_materno = alumno.apellido_materno
        alumno_db.matricula = alumno.matricula
        alumno_db.correo = alumno.correo

        # 🔐 Si viene password, se encripta
        if hasattr(alumno, "password") and alumno.password:
            alumno_db.password = hash_password(alumno.password)

        db.commit()
        db.refresh(alumno_db)

        return alumno_db

    except Exception:
        db.rollback()
        return None

    finally:
        db.close()


def eliminar(id):
    db: Session = SessionLocal()

    try:
        alumno = db.query(Alumno).filter(Alumno.id == id).first()

        if not alumno:
            return False

        db.delete(alumno)
        db.commit()

        return True

    except Exception:
        db.rollback()
        return False

    finally:
        db.close()


def filtrar_por_fecha(inicio, fin):
    db: Session = SessionLocal()

    try:
        return db.query(Alumno).filter(
            Alumno.fecha_alta >= inicio,
            Alumno.fecha_alta <= fin
        ).all()

    finally:
        db.close()