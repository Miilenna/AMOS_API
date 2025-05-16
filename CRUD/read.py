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
def get_saldo(id:int):
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT cartera FROM usuario WHERE id=%s;", (id,))
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

   # A DE COCHES (SIN ID)
def buscar_coches_filtrado(
    marca=None,
    modelo=None,
    anio=None,
    kilometraje_max=None,
    combustible=None,
    precio_min=None,
    precio_max=None,
    puertas=None,
    plazas=None
):
    conn = connexio()
    cur = conn.cursor()

    query = """
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
    """
    filtros = []
    valores = []

    if marca:
        filtros.append("marca ILIKE %s")
        valores.append(f"%{marca}%")
    if modelo:
        filtros.append("modelo ILIKE %s")
        valores.append(f"%{modelo}%")
    if anio:
        filtros.append("anio = %s")
        valores.append(anio)
    if kilometraje_max:
        filtros.append("kilometraje <= %s")
        valores.append(kilometraje_max)
    if combustible:
        filtros.append("combustible ILIKE %s")
        valores.append(f"%{combustible}%")
    if precio_min:
        filtros.append("precio >= %s")
        valores.append(precio_min)
    if precio_max:
        filtros.append("precio <= %s")
        valores.append(precio_max)
    if puertas:
        filtros.append("puertas = %s")
        valores.append(puertas)
    if plazas:
        filtros.append("plazas = %s")
        valores.append(plazas)

    if filtros:
        query += " WHERE " + " AND ".join(filtros)

    cur.execute(query, valores)
    resultados = cur.fetchall()

    cur.close()
    conn.close()

    return resultados
