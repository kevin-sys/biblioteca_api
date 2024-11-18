from fastapi import FastAPI
from app.database import Base, engine
from app.routers import books

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Crear la instancia de FastAPI
app = FastAPI(
    title="Biblioteca API",
    description="API para gestionar libros en una biblioteca.",
    version="1.0.0",
)

# Registrar los routers
app.include_router(books.router)

# Endpoint de prueba
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de la Biblioteca"}
