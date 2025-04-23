from connexio import connexio
import psycopg2

#PG INICIO, ANUNCIOS
def get_coche():
    conn=connexio()
    cur = conn.cursor()
    
    cur.execute("""SELECT marca, modelo, precio, anyo 
                FROM coche 
                JOIN usuario ON coche.id_pais = usuario.id_pais 
                WHERE usuario.id_pais = %s;""")
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text

#PG RESULTADOS
def get_coche_detallado():
    conn=connexio()
    cur = conn.cursor()
    
    cur.execute("""SELECT marca, modelo, anyo, kilometros, combustible, precio, caballos, puertas, version, plazas 
                FROM coche 
                JOIN usuario ON coche.id_pais = usuario.id_pais 
                WHERE usuario.id_pais = %s;""")
    text = cur.fetchall()
    
    cur.close()
    conn.close()
    
    return text


#PG REGISTRO
def get_usuario():
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT nombre, apellido, correo, contrasenya, direccion FROM usuario WHERE id=%s;")
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

#PG INICIO_SESION
def get_usuario():
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT nombre, contrasenya FROM usuario WHERE id=%s;")
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

#PG MOVIMIENTOS
def get_movimientos():
    conn = connexio()
    cur = conn.cursor()
    
    #añadir en la doc y en las tablas
    cur.execute("""
        SELECT m.tipo_movimiento, m.fecha_movimiento, d.valor, d.divisa
        FROM movimiento m
        JOIN divisa d ON m.id_divisa = d.id_divisa
        WHERE m.id_usuario = %s;
    """)
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
