from connexio import connexio
import psycopg2

def create_():
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = "INSERT INTO usuario () VALUES ();"
        values = ()
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Insert successful"}
    except Exception as e:
        # Retorna un error si la inserció falla
        return {"status": -1, "message": f"Error de connexió: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

