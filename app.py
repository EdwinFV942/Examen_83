from fastapi import FastAPI
from routes import alumno_routes, auth_routes

app = FastAPI(
    title="API Gestión de Alumnos",
    description="API para CRUD de alumnos con autenticación y filtros por fecha",
    version="1.0.0"
)

app.include_router(alumno_routes.router)
app.include_router(auth_routes.router)