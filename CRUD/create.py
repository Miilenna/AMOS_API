from connexio import connexio
import psycopg2
from .models import Usuario, Coche, Movimiento

#PG REGISTRO
def create_usuario(usuario: Usuario):    
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """INSERT INTO usuario (
            nombre,
            apellido,
            correo_electronico,
            fecha_nacimiento,
            contrasenya,
            direccion) VALUES (%s, %s, %s, %s, %s, %s);"""
        values = (usuario.nombre, usuario.apellido, usuario.correo_electronico, usuario.fecha_nacimiento, usuario.contrasenya, usuario.direccion)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#PG HACER_MOV
def create_movimiento(movimiento: Movimiento):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """INSERT INTO movimiento(
            tipo_movimiento,
            id_usuario,
            divisa,
            valor,
            region) VALUES (%s, %s, %s, %s, %s);"""
        values = (movimiento.tipo_movimiento, movimiento.id_usuario, movimiento.divisa, movimiento.valor, movimiento.region)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#PG ANUNCIOS INDIVIDUAL
def create_coche_detallado():
    conn=connexio()
    cur = conn.cursor()
    try:
        query= """INSERT INTO coche(
                    marca, 
                    modelo, 
                    any, 
                    kilometraje, 
                    combustible, 
                    precio, 
                    caballos, 
                    puertas, 
                    version, 
                    plazas)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        values = (Coche.marca, Coche.modelo, Coche.any, Coche.kilometros, Coche.combustible, Coche.precio, Coche.caballos, Coche.puertas, Coche.version, Coche.plazas)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
