import os
import psycopg2
from flask import g, Flask
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
 

def create_table_Hoteles():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Hoteles (
                id_hotel SERIAL PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                estrellas VARCHAR(10) NOT NULL,
                descripcion VARCHAR(500) NOT NULL,
                mail VARCHAR(30) NOT NULL,
                telefono VARCHAR(20) NOT NULL,
                activo BOOLEAN NOT NULL
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("Table created successfully")
    except Exception as e:
        print(f"Error: {e}")

    
def insert_hoteles(nombre, estrellas, descripcion, mail, telefono, activo):
    try:
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
        print("Hotel inserted successfully")
    except Exception as e:
        print(f"Error: {e}")
        

def get_completed_hoteles():
    try:
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
    except Exception as e:
        print(f"Error: {e}")
        return []


def get_archived_hoteles():
    try:
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
    except Exception as e:
        print(f"Error: {e}")
        return []

    
def get_all_hoteles():
    try:
        query = """
            SELECT * FROM Hoteles
            ORDER BY id_hotel
        """
        conn = psycopg2.connect(**DATABASE_CONFIG)
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        return results
    except Exception as e:
        print(f"Error: {e}")
        return []
  
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
    
app = Flask(__name__)
init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
    