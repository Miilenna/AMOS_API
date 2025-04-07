# Imports
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

def get_db_connection():
    return db_pool.get_connection()