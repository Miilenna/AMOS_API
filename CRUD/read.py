from connexio import connexio
import psycopg2

#1 --> función que selecciona el texto 'començar partida'
def get_usuario():
    conn = connexio()
    cur = conn.cursor()

    cur.execute("SELECT correo_electronico, contrasenya FROM usuario WHERE id=%s;")
    text = cur.fetchall()

    cur.close()
    conn.close()

    return text

