import os
import psycopg2
from flask import g
from dotenv import load_dotenv


load_dotenv()

print(os.getenv('DB_USERNAME'))

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', 5432)
}


def test_connection():
    conn = psycopg2.connect(
        host="localhost",
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    conn.commit()
    cur.close()
    conn.close()

    print("TEST CONECTION - OKAS")
    

def create_table_Hoteles():
    conn = psycopg2.connect(
        host = "localhost",
        user = os.getenv ('DB_USERNAME'),
        password = os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Hoteles (
            id_hotel SERIAL PRIMARY KEY,
            nombre varchar (50) NOT NULL,
            estrellas varchar (10) NOT NULL,
            descripcion varchar (500) NOT NULL,
            mail varchar (30) NOT NULL,
            telefono varchar (20) NOT NULL,
            activo BOOLEAN NOT NULL
        );
        """
    )
    conn.commit()
    
    cur.close()
    conn.close()
    
def insert_hoteles(nombre, estrellas, descripcion, mail, telefono, activo):
    query = """
        INSERT INTO Hoteles (nombre, estrellas, descripcion, mail, telefono, activo)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(query, (nombre, estrellas, descripcion, mail, telefono, activo))
    conn.commit()
    cur.close()
    conn.close()

def get_completed_hoteles():
    query = """
        SELECT * FROM Hoteles
        WHERE activo = true
        ORDER BY id_hotel
    """
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results 

def get_archived_hoteles():
    query = """
        SELECT * FROM Hoteles
        WHERE activo = false
        ORDER BY id_hotel
    """
    conn = psycopg2.connect(**DATABASE_CONFIG)
    cur = conn.cursor()
    cur.execute(query)
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results 
  
# Función para obtener la conexión a la base de datos
def get_db():
    # Si 'db' no está en el contexto global de Flask 'g'
    if 'db' not in g:
        # Crear una nueva conexión a la base de datos y guardarla en 'g'
        g.db = psycopg2.connect(**DATABASE_CONFIG)
    # Retornar la conexión a la base de datos
    return g.db

# Función para cerrar la conexión a la base de datos
def close_db(e=None):
    # Extraer la conexión a la base de datos de 'g' y eliminarla
    db = g.pop('db', None)
    # Si la conexión existe, cerrarla
    if db is not None:
        db.close()

# Función para inicializar la aplicación con el manejo de la base de datos
def init_app(app):
    # Registrar 'close_db' para que se ejecute al final del contexto de la aplicación
    app.teardown_appcontext(close_db)