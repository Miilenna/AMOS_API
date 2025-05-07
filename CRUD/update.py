from connexio import connexio
import psycopg2
from CRUD.models import Usuario, Coche, Movimiento, Divisa, UsuarioUpdate

        

#PG REGISTRO
def update_usuario(id: int, usuario: UsuarioUpdate):
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """UPDATE usuario SET 
            nombre = %s,
            apellido = %s,
            fecha_nacimiento = %s,
            contrasenya = %s,
            direccion = %s,
            cartera = %s
            WHERE id = %s"""
        values = (
            usuario.nombre,
            usuario.apellido,
            usuario.fecha_nacimiento,
            usuario.contrasenya,
            usuario.direccion,
            usuario.cartera,
            id
        )
        cur.execute(query, values)
        conn.commit()
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()
        conn.close()



#PG PERFIL
def update_perfil(contrasenya):    
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """UPDATE usuario SET (
            nombre,
            apellido,
            correo_electronico,
            fecha_nacimiento,
            direccion) = %s, %s, %s, %s, %s WHERE id = %s;"""
        cur.execute(query, (contrasenya))
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades


#PG ANUNCIOS
def update_coche_detallado(marca, modelo):
    conn=connexio()
    cur = conn.cursor()
    try:
        query= """UPDATE coche SET
                    marca, 
                    modelo, 
                    anyo, 
                    kilometros, 
                    combustible, 
                    precio, 
                    caballos, 
                    puertas, 
                    version, 
                    plazas = %s, %s, %s, %s, %s, %s, %s, %s, %s, %s WHERE id=%s;"""
        cur.execute(query, (marca, modelo))
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
        
        
#PG RESULTADOS
def update_coche_detallado():
    conn=connexio()
    cur = conn.cursor()
    try:
        query= """UPDATE coche SET
                    marca, 
                    modelo, 
                    anyo, 
                    kilometros, 
                    combustible, 
                    precio, 
                    caballos, 
                    puertas, 
                    version, 
                    plazas = %s, %s, %s, %s, %s, %s, %s, %s, %s, %s WHERE id=%s;"""
        cur.execute(query)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades