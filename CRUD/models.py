from pydantic import BaseModel
from typing import Optional
from datetime import date

class Usuario(BaseModel):
    nombre: str
    apellido: str
    correo_electronico: str
    fecha_nacimiento: date
    contrasenya: str
    direccion: str
    IBAN: Optional[str] = None
    cartera: Optional[float] = None
    
class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date]= None
    contrasenya: Optional[str] = None
    direccion: Optional[str] = None
    IBAN: Optional[str] = None
    cartera: Optional[float] = None

class Divisa (BaseModel):
	divisa: str
	valor: float
	region: str

class Coche(BaseModel):
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

class Movimiento(BaseModel):
	tipo_movimiento: str
	id_usuario: int
	fecha_movimiento: date
