from fastapi import FastAPI
from app.routers import users, citas, expedientes, recetas, especialidades
from app import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Registrar rutas
app.include_router(users.router, prefix="/api", tags=["Usuarios"])
app.include_router(citas.router, prefix="/api", tags=["Citas"])
app.include_router(expedientes.router, prefix="/api", tags=["Expedientes"])
app.include_router(recetas.router, prefix="/api", tags=["Recetas"])
app.include_router(especialidades.router, prefix="/api", tags=["Especialidades"])

# Punto de entrada
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
