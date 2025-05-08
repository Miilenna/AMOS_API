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

#PG ANUNCIOS
def delete_coche_detallado(marca, modelo):
    conn=connexio()
    cur = conn.cursor()
    try:
        query= "DELETE FROM coche WHERE id=%s"
        cur.execute(query, (marca, modelo))
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Eliminado correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
        
        
#PG RESULTADOS
def delete_coche_detallado():
    conn=connexio()
    cur = conn.cursor()
    try:
        query= "DELETE FROM coche WHERE id=%s"
        cur.execute(query)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Eliminado correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#PG INICIO, ANUNCIOS
def delete_coche():
    conn=connexio()
    cur = conn.cursor()
    try:
        query= "DELETE FROM coche WHERE id=%s"
        cur.execute(query)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Eliminado correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades