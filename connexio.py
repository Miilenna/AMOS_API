from mysql.connector import pooling

# Configura la connexió a MariaDB
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Pa123@77',
    'database': 'carplaytrade',
    'port': '3307',
    'collation': 'utf8mb4_general_ci'
}

# Pool de connexions
db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def connexio():
    return db_pool.get_connection()

""" import mysql.connector  # Asegúrate de importar mysql.connector
from mysql.connector import pooling
# Configura la connexió a MariaDB
def connexio():
    try:
        connection = mysql.connector.connect(
            host="10.2.53.190",
            user="seth",
            password="armeniaamos",
            database="carplaytrade"
            # Puedes descomentar y agregar más parámetros si es necesario
            # port=3306,
            # charset="utf8mb4",
            # use_pure=True,
            # ssl_disabled=True,
            # connection_timeout=30
        )
        return connection

    except mysql.connector.Error as e:
        print(f"Error al conectar: {e}")
        return None
 """
# Configura la connexió a MariaDB
