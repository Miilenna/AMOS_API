from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import connexio
import CRUD.read as read
import CRUD.update as update
import CRUD.create as create
import CRUD.delete as delete
from CRUD.models import Usuario, Divisa, Coche, Movimiento

app = FastAPI()
#----------------------------------USUARIO-------------------------------------------
@app.get("/get/usuarios", response_model=List[dict])
async def get_usuarios():
    usuarios = read.get_usuario_sesion()
    if not usuarios:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return usuarios

# CREATE - Crear usuario
@app.post("/post/usuarios")
async def create_usuario():
    result = create.create_usuario()
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

# UPDATE - Actualizar usuario
@app.put("/put/usuarios/{id}")
async def update_usuario(contrasenya: str):
    result = update.update_usuario(contrasenya)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

# DELETE - Eliminar usuario
@app.delete("/delete/usuarios/{id}")
async def delete_usuario(contrasenya: str):
    result = delete.delete_usuario(contrasenya)
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result

#------------------------------MOVIMIENTO-----------------------------------------------------
@app.get("/get/movimiento", response_model=List[dict])
async def get_movimiento():
    result = read.get_movimientos()
    if not result:
        raise HTTPException(status_code=404, detail="Usuarios no encontrados")
    return result

# CREATE - Crear usuario
@app.post("/post/movimiento")
async def create_movimiento():
    result = create.create_movimiento()
    if result["status"] != 1:
        raise HTTPException(status_code=500, detail=result["message"])
    return result


#------------------------------PERFIL----------------------------------------------------------------
@app.get("/get/perfil", response_model=List[dict])
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

