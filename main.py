from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import CRUD.read as read
import CRUD.update as update
import CRUD.create as create
import CRUD.delete as delete
from mysql.connector import pooling
from CRUD.models import Usuario, UsuarioUpdate, Movimiento, Divisa


app = FastAPI()

#----------------------------------USUARIO-------------------------------------------
@app.get("/get/usuarios/{id}")
async def get_usuarios(id: int):
    usuario = read.get_usuario_sesion(id)
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
async def create_movimiento(movimiento: Movimiento, divisa: Divisa):
    result = create.create_movimiento(movimiento, divisa)
    return result


#------------------------------PERFIL----------------------------------------------------------------
@app.get("/get/perfil")
async def get_perfil():
    result = read.get_usuario_registro()
    if not result:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return result

# CREATE - Crear usuario
@app.post("/post/perfil")
async def create_perfil():
    result = create.create_perfil()
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

# UPDATE - Actualizar usuario
@app.put("/put/perfil/{id}")
async def update_perfil(contrasenya: str):
    result = update.update_perfil(contrasenya)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

# DELETE - Eliminar usuario
@app.delete("/delete/perfil/{id}")
async def delete_perfil(contrasenya: str):
    result = delete.delete_perfil(contrasenya)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

#------------------------------------COCHE-----------------------------------------------------

