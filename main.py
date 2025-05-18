from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import CRUD.read as read
import CRUD.update as update
import CRUD.create as create
import CRUD.delete as delete
from mysql.connector import pooling
from fastapi.middleware.cors import CORSMiddleware
from CRUD.models import Usuario, UsuarioUpdate, Movimiento, PerfilUpdate, Coche
from fastapi import Body
from typing import Dict, Any

app = FastAPI()

# Configuración CORS actualizada
origins = [
    "http://localhost:8082",
    "http://127.0.0.1:8082",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
    "http://127.0.0.1:63314"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/ping")
def ping():
    return {"status": "ok"}

#----------------------------------USUARIO-------------------------------------------
@app.get("/get/usuarios/{email}")
async def get_usuarios(email: str):
    # Tu lógica para obtener el usuario
    usuario = read.get_usuario_sesion(email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.get("/get/usuario_id/{email}/{contrasenya}")
async def get_usuarios_id(email: str, contrasenya: str):
    # Tu lógica para obtener el usuario
    usuario = read.get_usuario_sesion_conID(email, contrasenya)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# CREATE - Crear usuario
@app.post("/post/usuarios")
async def create_usuario(usuario: Usuario):
    resultado = create.create_usuario(usuario)
    return resultado

# UPDATE - Actualizar usuario
@app.put("/put/usuarios/{id}")
async def update_usuario(id: int, usuario: UsuarioUpdate):
    result = update.update_usuario(id, usuario)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result


# DELETE - Eliminar usuario
@app.delete("/delete/usuarios/{contrasenya}")
async def delete_usuario(id: int):
    result = delete.delete_usuario(id)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

#------------------------------MOVIMIENTO-----------------------------------------------------
@app.get("/get/movimiento")
async def get_movimiento(id: int):
    result = read.get_movimientos(id)
    if not result:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return result

# CREATE - Crear usuario
@app.post("/post/movimiento")
async def create_movimiento(movimiento: Movimiento):
    result = create.create_movimiento(movimiento)
    return result


#------------------------------PERFIL----------------------------------------------------------------
@app.get("/get/perfil/{id}")
async def get_perfil(id: int):
    perfil = read.get_usuario_registro(id)
    if not perfil:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return perfil

# UPDATE - Actualizar usuario
@app.put("/put/perfil/{contrasenya}")
async def update_perfil(contrasenya: str, perfil: PerfilUpdate):
    result = update.update_perfil(contrasenya, perfil)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result
#------------------------------------COCHE-----------------------------------------------------
@app.get("/get/coche/{id_coche}")
async def get_coche(id_coche: int):
    coche = read.get_coche(id_coche)
    if not coche:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return coche

@app.get("/get/coche_detallado/{id_coche}")
async def get_coche_detallado(id_coche: int):
    coche = read.get_coche_detallado(id_coche)
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche

@app.get("/get/coche_detallado_id_usuario/{id_usuario}")
async def get_coches_por_usuario(id_usuario: int):
    coche = read.get_coches_por_usuario(id_usuario)
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche

@app.put("/put/coche_detallado/{id_coche}")
async def update_coche(id_coche: int, coche: Coche):
    result = update.update_coche_detallado(id_coche, coche)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

@app.post("/post/coche_detallado")
async def create_coche(coche: Coche):
    result = create.create_coche_detallado(coche)
    return result

@app.delete("/delete/coche/{id_coche}")
async def delete_coche(id_coche: int):
    result = delete.delete_coche_detallado(id_coche)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result



@app.get("/get/buscar_coches_filtrado")
async def buscar_coches_filtrado(
    marca: Optional[str] = None,
    modelo: Optional[str] = None,
    anioMin: Optional[int] = None,  # Filtro año mínimo
    anioMax: Optional[int] = None,  # Filtro año máximo
    kilometraje_max: Optional[int] = None,  # Filtro km máximo
    precio_min: Optional[int] = None,  # Filtro precio mínimo
    precio_max: Optional[int] = None,  # Filtro precio máximo
    combustible: Optional[str] = None,
    puertas: Optional[int] = None,
    plazas: Optional[int] = None
):
    resultados = read.buscar_coches_filtrado(
        marca=marca,
        modelo=modelo,
        anioMin=anioMin,
        anioMax=anioMax,
        kilometraje_max=kilometraje_max,
        precio_min=precio_min,
        precio_max=precio_max,
        combustible=combustible,
        puertas=puertas,
        plazas=plazas
    )
    
    # Convertir resultados SQL a JSON
    columnas = ["id", "marca", "modelo", "anio", "kilometraje", "precio", "combustible"]
    return [{col: val for col, val in zip(columnas, row)} for row in resultados]
#----------------------------------------CARTERA--------------------------------------------
@app.get("/get/saldo/{id}")
async def get_saldo(id: int):
    coche = read.get_saldo(id)
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche