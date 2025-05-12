import psycopg2
from mysql.connector import pooling;

# Función para establecer una conexión con la base de datos PostgreSQL
def connexio():
    return psycopg2.connect(
        database = "carplaytrade",
        user = "milena",
        password = "mh1l3n4a",
        host = "192.168.35.5",
        port = "8443"
    )

db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def connexio():
    return db_pool.get_connection()



# {
#   "nombre": "Milena",
#   "apellido": "Vardumyan",
#   "correo_electronico": "milena@gmail.com",
#   "fecha_nacimiento": "2004-12-19",
#   "contrasenya": "345",
#   "direccion": "calle barcelona 12, Barcelona",
#   "IBAN": "ES1234567890",
#   "cartera": 1530
# }