from connexio import connexio
import psycopg2
        
#PG REGISTRO
def delete_usuario(id: int):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = "DELETE FROM usuario WHERE contrasenya=%s"
        cur.execute(query,(id,))
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Eliminado correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#PG ANUNCIOS INDIVIDUAL
def delete_coche_detallado(id_coche: int):
    conn=connexio()
    cur = conn.cursor()
    try:
        query= "DELETE FROM coche WHERE id=%s"
        cur.execute(query, (id_coche,))
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Eliminado correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades