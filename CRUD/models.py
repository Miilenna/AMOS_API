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
    
class PerfilUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    fecha_nacimiento: Optional[date]= None
    direccion: Optional[str] = None
    IBAN: Optional[str] = None
class Movimiento(BaseModel):
	tipo_movimiento: str
	id_usuario: int
	divisa: str
	valor: float
	region: str 
class Coche(BaseModel):
    id_usuario: Optional[int] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    anio: Optional[int] = None
    kilometraje: Optional[int] = None
    combustible: Optional[int] = None
    precio: Optional[int] = None
    matricula: Optional[str] = None
    caballos: Optional[int] = None
    puertas: Optional[int] = None
    version: Optional[str] = None
    plazas: Optional[int] = None
