from connexio import connexio
import psycopg2

#-----------------------------ACTUALITZAR COMENÇAR PARTIDA------------------------------------
def update_començar(paraula, id):
    conn = connexio()
    cur = conn.cursor()
    try:
        # Actualitza la columna "texts_joc" de la taula "informació" per a un registre específic identificat per l'id
        query = "UPDATE informació SET texts_joc = %s WHERE id = %s;"
        cur.execute(query, (paraula, id))  # Passa els paràmetres paraula i id a la consulta
        conn.commit() 
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#-----------------------------ACTUALITZAR PARAULA SECRETA------------------------------------
def update_començar_paraula(paraula, id):
    conn = connexio()
    cur = conn.cursor()
    try:
        query = "UPDATE informació SET texts_joc = %s WHERE id = %s;"
        cur.execute(query, (paraula, id)) 
        conn.commit()  
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  
        conn.close()  

#-----------------------------ACTUALITZAR ABECEDARI------------------------------------
def update_abecedari(lletres, id_alfabet):
    conn = connexio()
    cur = conn.cursor()
    try:
        # Actualitza la columna "lletres" de la taula "alfabet" per a un registre específic identificat per id_alfabet
        query = "UPDATE alfabet SET lletres = %s WHERE id_alfabet = %s;"
        cur.execute(query, (lletres, id_alfabet))  # Passa els paràmetres lletres i id_alfabet a la consulta
        conn.commit()
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
