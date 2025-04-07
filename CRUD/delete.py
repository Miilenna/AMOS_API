from connexio import connexio
import psycopg2

#-----------------------------ELIMINAR PARAULA------------------------------------
def delete_paraula(id):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        # Elimina una fila de la taula "informació" basada en l'id proporcionat
        query = "DELETE FROM informació WHERE id = %s;"
        cur.execute(query, (id,))  # Passa el paràmetre id a la consulta
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Delete successful"}
    except Exception as e:
        # Mostra un error si la eliminació falla
        print(f"Error during deletion: {e}")
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#-----------------------------ELIMINAR ABECEDARI------------------------------------
def delete_alfabet(id_alfabet):
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        # Elimina una fila de la taula "alfabet" basada en l'id_alfabet proporcionat
        query = "DELETE FROM alfabet WHERE id_alfabet = %s;"
        cur.execute(query, (id_alfabet,))  # Passa el paràmetre id_alfabet a la consulta
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Delete successful"}
    except Exception as e:
        # Mostra un error si la eliminació falla
        print(f"Error during deletion: {e}")
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió
