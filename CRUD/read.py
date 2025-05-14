from connexio import connexio
import psycopg2

#PG INICIO, RESULTADOS
def get_coche(id_coche: int):
    conn=connexio()
    cur = conn.cursor()
    
    cur.execute("""
            SELECT 
                id_usuario,
                marca,
                modelo,
                anio,
                precio,
                matricula
            FROM coche 
            WHERE id = %s;
        """, (id_coche,))
    coche_data = cur.fetchone()    
    
    cur.close()
    conn.close()
    
    return coche_data

#PG ANUNCIOS INDIVIDUAL
def get_coche_detallado(id_coche: int):
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            id_usuario,  
            stock,
            marca,      
            modelo,      
            anio,        
            kilometraje, 
            combustible,
            precio,     
            matricula,
            caballos,  
            puertas,    
            version,    
            plazas       
        FROM coche 
        WHERE id = %s;
    """, (id_coche,))
    
    coche_data = cur.fetchone()  
    cur.close()
    conn.close()
    
    return coche_data 

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
def get_usuario_sesion(email: str):
    conn = connexio()
    cur = conn.cursor()
    cur.execute("SELECT nombre, contrasenya FROM usuario WHERE correo_electronico=%s;", (email,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return {"nombre": result[0], "contrasenya": result[1]}
    else:
        return None  


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
def get_saldo(id:int):
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT cartera FROM usuario WHERE id=%s;", (id,))
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text
