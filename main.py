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

origins = [
    "http://localhost:8082",
    "http://localhost:8082",
    "http://localhost:8081",
    "http://127.0.0.1:8081",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
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
    usuario = read.get_usuario_sesion(email)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@app.post("/post/usuario")
async def create_usuario(usuario: Usuario):
    resultado = create.create_usuario(usuario)
    return resultado

@app.put("/put/usuarios/{id}")
async def update_usuario(id: int, usuario: UsuarioUpdate):
    result = update.update_usuario(id, usuario)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result


@app.delete("/delete/usuarios/{id}") 
async def delete_usuario(id: int): 
    result = delete.delete_usuario(id)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

#------------------------------MOVIMIENTO-----------------------------------------------------
@app.get("/get/movimiento/{id_usuario}") 
async def get_movimiento(id_usuario: int):
    result = read.get_movimientos(id_usuario)
    if not result:
        raise HTTPException(status_code=404, detail="Movimientos no encontrados") 
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
        raise HTTPException(status_code=404, detail="Perfil no encontrado")
    return perfil

@app.put("/put/perfil/{id}") 
async def update_perfil(id: int, perfil: PerfilUpdate): 
    result = update.update_perfil(id, perfil) 
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result
#------------------------------------COCHE-----------------------------------------------------

@app.get("/get/coche/{id_coche}")
async def get_coche(id_coche: int):
    coche = read.get_coche(id_coche)  
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche

@app.get("/get/coche/det/{id_coche}")
async def get_coche_detallado(id_coche: int):
    coche = read.get_coche_detallado(id_coche)  
    if not coche:
        raise HTTPException(status_code=404, detail="Coche no encontrado")
    return coche

@app.get("/get/coches_usuario/{id_usuario}")
async def get_coches_usuario(id_usuario: int):
    coches = read.get_coches_usuario(id_usuario)  
    if not coches:
        raise HTTPException(status_code=404, detail="No se encontraron coches para el usuario")
    return coches

@app.get("/get/coches_detallados_inicio/")
async def get_coches_detallados_inicio():
    coches = read.get_coche_detallado_inicio()  
    if not coches:
        raise HTTPException(status_code=404, detail="No se encontraron coches")
    return coches

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

@app.put("/put/buscar_coches_filtrado")
async def buscar_coches_filtrado(filtros: Dict[str, Any] = Body(...)):
    resultados = read.buscar_coches_filtrado(
        marca=filtros.get("marca"),
        modelo=filtros.get("modelo"),
        anio=filtros.get("anioMin"), 
        kilometraje_max=filtros.get("kilometraje_max"),
        combustible=filtros.get("combustible"),
        precio_min=filtros.get("precio_min"),
        precio_max=filtros.get("precio_max"),
        puertas=filtros.get("puertas"),
        plazas=filtros.get("plazas")
    )
    return resultados
#----------------------------------------CARTERA--------------------------------------------
@app.get("/get/saldo/{id}")
async def get_saldo(id: int):
    saldo = read.get_saldo(id) 
    if not saldo:
        raise HTTPException(status_code=404, detail="Saldo no encontrado") # Corrected message
    return saldo