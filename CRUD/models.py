from pydantic import BaseModel
from typing import Optional
from datetime import date

class Usuario(BaseModel):
    id: int
    nombre: str
    apellido: str
    correo_electronico: str
    fecha_nacimiento: date
    contrasenya: str
    direccion: str

class Divisa (BaseModel):
	id: int
	divisa: str
	valor: str
	region: str

class Coche(BaseModel):
	id: int
	id_usuario: int
	marca: str
	modelo: str
	any: int
	kilometros: int
	combustible: int
	precio: int
	caballos: int
	puertas: int
	version: str
	plazas: int

class Movimiento (BaseModel):
	id: int
	tipo_movimiento: str
	id_usuario: int
	fecha_movimiento: date
