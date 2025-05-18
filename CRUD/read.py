from connexio import connexio
import psycopg2

#PG INICIO, RESULTADOS
def get_coche(id: int):
    conn = connexio()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            id,
            id_usuario,
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
    """, (id,))
    coche_data = cur.fetchone()  
    cur.close()
    conn.close()
    
    return coche_data
      

#PG ANUNCIOS INDIVIDUAL
def get_coche_detallado(id: int):
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            id,
            id_usuario,
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
    """, (id,))
    
    coche_data = cur.fetchone()  
    cur.close()
    conn.close()
    
    return coche_data 

def get_coches_usuario(id_usuario: int):
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            id,
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
    
    coches_data = cur.fetchall()
    cur.close()
    conn.close()
    
    return coches_data

def get_coche_detallado_inicio():
    conn = connexio()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            id,
            marca,      
            modelo,      
            anio,        
            kilometraje, 
            combustible,
            precio,     
            caballos,  
            puertas,    
            version,    
            plazas       
        FROM coche;
    """)
    
    coches_data = cur.fetchall()  
    
    column_names = [desc[0] for desc in cur.description]
    result = [dict(zip(column_names, row)) for row in coches_data]
    
    cur.close()
    conn.close()
    
    return result 

#PG REGISTRO
def get_usuario_registro(id: int):
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT nombre, apellido, correo_electronico, fecha_nacimiento, contrasenya, IBAN, cartera, direccion FROM usuario WHERE id=%s;", (id,))
    text = cur.fetchone()

    cur.close()
    conn.close()

    return text

#PG INICIO_SESION
def get_usuario_sesion(email: str):
    conn = connexio()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, contrasenya FROM usuario WHERE correo_electronico=%s;", (email,))
    result = cur.fetchone()
    cur.close()
    conn.close()

    if result:
        return {"id": result[0], "nombre": result[1], "contrasenya": result[2]}
    else:
        return None 


#PG MOVIMIENTOS
def get_movimientos(id_usuario: int):
    conn = connexio()
    cur = conn.cursor(dictionary=True)
    
    cur.execute("""
        SELECT
            tipo_movimiento,
            valor,
            divisa,
            region,
            fecha_movimiento
            FROM movimiento
            WHERE id_usuario = %s
            ORDER BY fecha_movimiento DESC
    """, (id_usuario,))
    text = cur.fetchall()
    
    for mov in text:
        mov["fecha_formateada"] = mov["fecha_movimiento"].strftime("%d/%m/%Y %H:%M")
    
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
