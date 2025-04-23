from connexio import connexio
import psycopg2



#PG REGISTRO
def create_usuario():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    correo_electronico = input("Introduce el correo electrónico: ")
    fecha_nacimiento = input("Introduce la fecha de nacimiento (YYYY-MM-DD): ")
    contrasenya = input("Introduce la contraseña: ")
    direccion = input("Introduce la dirección: ")
    
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """UPDATE usuario SET (
            nombre,
            apellido,
            correo_electronico,
            fecha_nacimiento,
            contrasenya,
            direccion) VALUES (%s, %s, %s, %s, %s, %s);"""
        values = (nombre, apellido,correo_electronico,fecha_nacimiento,contrasenya,direccion)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
        
        
#PG HACER_MOV
def create_movimiento():
    tipo_movimiento = input("Introduce el tipo de movimiento que quieres hacer: ")
    divisa = input("Introduce el tipo de divisa: ")
    valor = input("Introduce la cuantia del movimiento: ")
    
    # Estableix una connexió amb la base de dades
    conn = connexio()
    cur = conn.cursor()
    try:
        query = """INSERT INTO movimiento (
            tipo_movimiento
            divisa,
            valor) VALUES (%s, %s, %s);"""
        values = (tipo_movimiento, divisa, valor)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

#PG PERFIL
def create_perfil():
    nombre = input("Introduce el nombre: ")
    apellido = input("Introduce el apellido: ")
    correo_electronico = input("Introduce el correo electrónico: ")
    fecha_nacimiento = input("Introduce la fecha de nacimiento (YYYY-MM-DD): ")
    direccion = input("Introduce la dirección: ")
    
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
        values = (nombre, apellido,correo_electronico,fecha_nacimiento,direccion)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades
        
#PG ANUNCIOS
def create_coche_detallado():
    marca = input("Introduce la marca: ")
    modelo = input("Introduce el modelo: ")
    anyo = input("Introduce el año: ")
    kilometros = input("Introduce el kilometraje: ")
    combustible = input("Introduce el combustible: ")
    precio = input("Introduce el precio: ")
    caballos = input("Introduce los caballos: ")
    puertas = input("Introduce las puertas: ")
    version = input("Introduce la versión: ")
    plazas = input("Introduce las plazas: ")
    
    conn=connexio()
    cur = conn.cursor()
    try:
        query= """INSERT INTO (
                    marca, 
                    modelo, 
                    anyo, 
                    kilometros, 
                    combustible, 
                    precio, 
                    caballos, 
                    puertas, 
                    version, 
                    plazas)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        values = (marca, modelo, anyo, kilometros, combustible, precio, caballos, puertas, version, plazas)
        cur.execute(query, values)
        conn.commit()  # Confirma els canvis
        return {"status": 1, "message": "Actualitzat correctament"}
    except Exception as e:
        return {"status": 0, "message": f"Error: {e}"}
    finally:
        cur.close()  # Tanca el cursor
        conn.close()  # Tanca la connexió amb la base de dades

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
