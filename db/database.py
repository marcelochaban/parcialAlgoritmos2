import sqlite3

# Nombre de la base de datos SQLite
DATABASE = 'inventario.db'

def get_db():
    """
    Establece una conexión con la base de datos SQLite.

    Retorna:
        conn (sqlite3.Connection): Una conexión a la base de datos 'inventario.db'.
    """
    # Conecta a la base de datos especificada y devuelve el objeto de conexión
    conn = sqlite3.connect(DATABASE)
    return conn
