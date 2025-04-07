from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from connexio import connexio
import CRUD.read as read
import CRUD.update as update
import CRUD.create as create
import CRUD.delete as delete

app = FastAPI()

#-----------------------------ESQUEMA INFORMACIÓ------------------------------------
class Informacion(BaseModel):
    correo_electronico: str  # Nombre total d'intents disponibles al joc
    contrasenya: str  # Text relacionat amb el joc (p. ex., una pista o paraula clau)

#----------------------------------GET-------------------------------------------
# Endpoint que retorna el text del botó "començar partida"
@app.get("/usuario", response_model=List[dict])
async def get_usuario():
    text = read.get_usuario()  # Recupera el text inicial de la base de dades
    if not text:
        raise HTTPException(status_code=404, detail="No s'han trobat")
    return text # Retorna els resultats en format JSON

#----------------------------------POST-------------------------------------------
# Endpoint que retorna el nombre d'intents i l'incrementa
@app.post("/intents", response_model=List[dict])
async def intents():
    intents = read.get_intents()  # Recupera el nombre d'intents
    if not intents: 
        raise HTTPException(status_code=404, detail="No s'han trobat els intents")
    return word_schema(intents)  # Retorna els resultats en format JSON

#----------------------------------PUT-------------------------------------------
# Endpoint per actualitzar el text de partida
@app.put("/comencar_update/{id}")
async def update_start(id: int, paraula: str):
    result = update.update_començar(id, paraula)  # Actualitza el text
    if not result:
        raise HTTPException(status_code=400, detail="No s'ha pogut fer l'actualització")
    return {"message": "Actualitzat correctament"}

#----------------------------------DELETE-------------------------------------------
# Endpoint per eliminar informació de la partida
@app.delete("/comencar_delete/{id}")
async def delete_paraula(id: int):
    result = delete.delete_paraula(id)  # Elimina la informació de la partida
    if result.get("status") != 1:
        raise HTTPException(status_code=400, detail="No s'ha pogut eliminar la informació")
    return {"message": "Eliminat correctament"}

# Endpoint per eliminar un abecedari
@app.delete("/abecedari_delete/{id_alfabet}")
async def delete_alfabet(id_alfabet: int):
    result = delete.delete_alfabet(id_alfabet)  # Elimina l'abecedari
    if result.get("status") != 1:
        raise HTTPException(status_code=400, detail="No s'ha pogut eliminar l'abecedari")
    return {"message": "Eliminat correctament"}
