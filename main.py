from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import CRUD.read as read
import CRUD.update as update
import CRUD.create as create
import CRUD.delete as delete
from mysql.connector import pooling
from CRUD.models import Usuario, UsuarioUpdate, Movimiento, PerfilUpdate


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
