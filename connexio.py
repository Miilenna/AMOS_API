import connexio
from mysql.connector import pooling

# Configura la connexió a MariaDB
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Pa123@77',
    'database': 'divises',
    'port': '3307',
    'collation': 'utf8mb4_general_ci'
}

# Pool de connexions
db_pool = pooling.MySQLConnectionPool(pool_name="mypool", pool_size=5, **db_config)

def get_db_connection():
    return db_pool.get_connection()