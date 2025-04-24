from connexio import connexio
import psycopg2
from .models import Usuario, Coche, Movimiento, Divisa

#PG REGISTRO
def create_usuario():    
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
        values = (Usuario.nombre, Usuario.apellido, Usuario.correo_electronico, Usuario.fecha_nacimiento, Usuario.contrasenya, Usuario.direccion)
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
def create_movimiento():
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """INSERT INTO movimiento (
            tipo_movimiento
            divisa,
            valor) VALUES (%s, %s, %s);"""
        values = (Movimiento.tipo_movimiento, Divisa.divisa, Divisa.valor)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#PG PERFIL
def create_perfil():
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """INSERT INTO usuario (
            nombre,
            apellido,
            correo_electronico,
            fecha_nacimiento,
            direccion) VALUES (%s, %s, %s, %s, %s);"""
        values = (Usuario.nombre, Usuario.apellido, Usuario.correo_electronico, Usuario.fecha_nacimiento, Usuario.direccion)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
        
#PG ANUNCIOS
def create_coche_detallado():
    conn=connexio()
    cur = conn.cursor()
    try:
        query= """INSERT INTO coche(
                    marca, 
                    modelo, 
                    any, 
                    kilometros, 
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
