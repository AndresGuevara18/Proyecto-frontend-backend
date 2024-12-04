#comandp iniciar -- uvicorn main:app --reload
from fastapi import FastAPI
from user import router
from fastapi.middleware.cors import CORSMiddleware #conectar con front

#lista origenes que permite acceso sera un array
origins = [
    "http://localhost:5173" #fornt se puede mas de un origen
] 

app = FastAPI() #instancia de FastAPI

# Configurar solicitudes entre el frontend y el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes
    allow_credentials=True, # Permitir envío de cookies/credenciales en las solicitudes
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"], # Permitir todos los encabezados (Content-Type, Authorization)
)#senbrando middleware

app.include_router(router) # Incluir  rutas definidas en `user.py` utilizando su router

#ruta raíz que responde a solicitudes GET en "/"
@app.get("/")
async def root(): #función  asíncrona
    return {"message": "Esta es mi API con FastAPI"}