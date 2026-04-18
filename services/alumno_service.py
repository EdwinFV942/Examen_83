from repository import alumno_repository

def crear(alumno):
    return alumno_repository.guardar(alumno)

def obtener():
    return alumno_repository.obtener_todos()

def actualizar(id, alumno):
    return alumno_repository.actualizar(id, alumno)

def eliminar(id):
    return alumno_repository.eliminar(id)

def filtrar(inicio, fin):
    return alumno_repository.filtrar_por_fecha(inicio, fin)