from connexio import connexio
import psycopg2
        

#PG REGISTRO
def update_usuario(contrasenya):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """UPDATE usuario SET 
            nombre,
            apellido,
            correo_electronico,
            fecha_nacimiento,
            contrasenya,
            direccion = %s, %s, %s, %s, %s, %s WHERE id = %s"""
        cur.execute(query,(contrasenya))
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades


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