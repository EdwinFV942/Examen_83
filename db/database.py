from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 REEMPLAZA TU PASSWORD Y DB
DATABASE_URL = "mysql+pymysql://admin:db_examen@examen-backend-db.cd084u2s2kv7.us-east-2.rds.amazonaws.com:3306/examen"

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # 🔥 evita errores de conexión
    connect_args={
        "ssl": {
            "ca": "global-bundle.pem"  # 🔥 certificado AWS
        }
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# 🔥 dependencia FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()