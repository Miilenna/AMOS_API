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
def update_perfil(id_usuario: int, perfil: PerfilUpdate):    
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """
            UPDATE usuario 
            SET 
                nombre = %s,
                apellido = %s,
                fecha_nacimiento = %s,
                IBAN = %s,
                direccion = %s
            WHERE id = %s;
        """
        
        # Valores en el orden correcto
        values = (
            perfil.nombre,
            perfil.apellido,
            perfil.fecha_nacimiento,
            perfil.IBAN,
            perfil.direccion,
            id_usuario
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
        
#PG ANUNCIOS INDIVIDUAL
def update_coche_detallado(id_coche: int, coche: Coche):
    conn=connexio()
    cur = conn.cursor()
    try:
        query= """UPDATE coche SET 
                    id_usuario = %s,  
                    marca = %s,      
                    modelo = %s,      
                    anio=%s,        
                    kilometraje=%s, 
                    combustible=%s,
                    precio=%s,     
                    matricula=%s,
                    caballos=%s,  
                    puertas=%s,    
                    version=%s,    
                    plazas=%s
                WHERE id = %s"""
     
        values = (
            coche.id_usuario,
            coche.marca,
            coche.modelo,
            coche.anio,
            coche.kilometraje,
            coche.combustible,
            coche.precio,
            coche.matricula,
            coche.caballos,
            coche.puertas,
            coche.version,
            coche.plazas,
            id_coche
        )
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades