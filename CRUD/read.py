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
    
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        # Devuelve una lista de un solo diccionario para que la respuesta sea un array JSON
        keys = [
            "id_usuario", "stock", "marca", "modelo", "anio", "kilometraje",
            "combustible", "precio", "matricula", "caballos", "puertas", "version", "plazas"
        ]
        return [dict(zip(keys, row))]
    else:
        return []

def get_coches_por_usuario(id_usuario: int):
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            id,  
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
        WHERE id_usuario = %s;
    """, (id_usuario,))
    
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    keys = [
        "id", "stock", "marca", "modelo", "anio", "kilometraje",
        "combustible", "precio", "matricula", "caballos", "puertas", "version", "plazas"
    ]
    # Return a list of dicts, one per row
    return [dict(zip(keys, row)) for row in rows]

#PG REGISTRO
def get_usuario_registro(id: int):
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT nombre, apellido, correo_electronico, fecha_nacimiento, contrasenya, IBAN, cartera, direccion FROM usuario WHERE id=%s;", (id,))
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
    # Ensure all results are read to avoid "Unread result found" error
    cur.fetchall()

    cur.close()
    conn.close()

    if result:
        # Return as a list of dicts to match expected JSON array
        return [{"nombre": result[0], "contrasenya": result[1]}]
    else:
        return []

def get_usuario_sesion_conID(email: str, contrasenya: str):
    conn = connexio()
    cur = conn.cursor()
    cur.execute("SELECT id FROM usuario WHERE correo_electronico=%s and contrasenya=%s;", (email, contrasenya,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        return {"id": result[0]}
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

   # A DE COCHES (SIN ID)
def buscar_coches_filtrado(
    marca=None,
    modelo=None,
    anioMin=None,
    anioMax=None,
    kilometraje_max=None,
    precio_min=None,
    precio_max=None,
    combustible=None,
    puertas=None,
    plazas=None
):
    conn = connexio()
    cur = conn.cursor()

    query = """
        SELECT 
            id, marca, modelo, anio, 
            kilometraje, precio, combustible
        FROM coche
    """
    filtros = []
    valores = []

    # Filtro por marca y modelo (LIKE para búsqueda parcial)
    if marca:
        filtros.append("marca LIKE %s")
        valores.append(f"%{marca}%")
    if modelo:
        filtros.append("modelo LIKE %s")
        valores.append(f"%{modelo}%")

    # Filtro por rango de AÑO
    if anioMin is not None and anioMax is not None:
        filtros.append("anio BETWEEN %s AND %s")
        valores.extend([anioMin, anioMax])
    elif anioMin is not None:
        filtros.append("anio >= %s")
        valores.append(anioMin)
    elif anioMax is not None:
        filtros.append("anio <= %s")
        valores.append(anioMax)

    # Filtro por KILOMETRAJE (hasta el máximo)
    if kilometraje_max is not None:
        filtros.append("kilometraje <= %s")
        valores.append(kilometraje_max)

    # Filtro por rango de PRECIO
    if precio_min is not None and precio_max is not None:
        filtros.append("precio BETWEEN %s AND %s")
        valores.extend([precio_min, precio_max])
    elif precio_min is not None:
        filtros.append("precio >= %s")
        valores.append(precio_min)
    elif precio_max is not None:
        filtros.append("precio <= %s")
        valores.append(precio_max)

    # Otros filtros
    if combustible:
        filtros.append("combustible = %s")
        valores.append(combustible)
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
    conn.close()
    return resultados
