from connexio import connexio
import psycopg2

#PG INICIO, ANUNCIOS
def get_coche(id_coche: int):
    conn=connexio()
    cur = conn.cursor()
    
    cur.execute("""
            SELECT 
                id_usuario,
                marca,
                modelo,
                anio,
                precio
            FROM coche 
            WHERE id = %s;
        """, (id_coche,))
    coche_data = cur.fetchone()    
    
    cur.close()
    conn.close()
    
    return coche_data

#PG RESULTADOS
def get_coche_detallado():
    conn=connexio()
    cur = conn.cursor()
    
    cur.execute("""SELECT marca, modelo, anio, kilometros, combustible, precio, caballos, puertas, version, plazas 
                FROM coche 
                JOIN usuario ON coche.id_pais = usuario.id_pais 
                WHERE usuario.id_pais = %s;""")
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text


#PG REGISTRO
def get_usuario_registro(id: int):
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT nombre, apellido, correo_electronico, fecha_nacimiento, contrasenya, direccion, IBAN, cartera FROM usuario WHERE id=%s;", (id,))
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

#PG INICIO_SESION
def get_usuario_sesion(id: int):
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT nombre, contrasenya FROM usuario WHERE id=%s;", (id,))
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

#PG MOVIMIENTOS
def get_movimientos(id: int):
    conn = connexio()
    cur = conn.cursor()
    
    #añadir en la doc y en las tablas
    cur.execute("""
        SELECT tipo_movimiento, fecha_movimiento, valor, divisa
        FROM movimiento 
        WHERE id_usuario = %s;
    """, (id,))
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text

#PG SALDO
def get_saldo():
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT cartera FROM usuario WHERE id=%s;")
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text
