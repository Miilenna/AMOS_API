from connexio import connexio
import psycopg2
from CRUD.models import Usuario, Coche, Movimiento, UsuarioUpdate, PerfilUpdate

        

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
def update_perfil(contrasenya: str, perfil: PerfilUpdate):    
    conn = connexio()
    cur = conn.cursor()
    try:
        # Consulta SQL corregida para MariaDB/MySQL
        query = """
            UPDATE usuario 
            SET 
                nombre = %s,
                apellido = %s,
                fecha_nacimiento = %s,
                direccion = %s,
                IBAN = %s
            WHERE contrasenya = %s;
        """
        
        # Valores en el orden correcto
        values = (
            perfil.nombre,
            perfil.apellido,
            perfil.fecha_nacimiento,
            perfil.direccion,
            perfil.IBAN,
            contrasenya
        )
        
        cur.execute(query, values)
        conn.commit()
        return {"status": 1, "message": "Actualizado correctamente"}
    except Exception as e:
        conn.rollback()
        return {"status": 0, "message": f"Error: {str(e)}"}
    finally:
        cur.close()
        conn.close()
        
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