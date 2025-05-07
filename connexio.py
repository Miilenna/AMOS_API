import psycopg2
from mysql.connector import pooling

# Configura la connexió a MariaDB
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'carplaytrade',
    'port': '3308',
    'collation': 'utf8mb4_general_ci'
}

# Pool de connexions
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