# Imports
import psycopg2

# Función para establecer una conexión con la base de datos PostgreSQL
def connexio():
    return psycopg2.connect(
        database = "carplaytrade",
        user = "milena",
        password = "mh1l3n4a",
        host = "localhost",
        port = "5432"
    )