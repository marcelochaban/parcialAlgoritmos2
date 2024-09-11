import sqlite3
from models.client_model import Client
from db.database import get_db


def get_all_clients():
    """
    Obtiene todos los clientes desde la base de datos.

    Devuelve:
        - Una lista de objetos `Client`, donde cada objeto representa un cliente en la base de datos.
    """

    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, telefono, email FROM clientes')
        clients = cursor.fetchall()
        return [Client(id=row[0], name=row[1], phone=row[2], email=row[3]) for row in clients]

def get_client_by_id(client_id):
    """
    Obtiene un cliente específico desde la base de datos utilizando su ID.

    Parámetros:
        - client_id (int): El ID del cliente a obtener.

    Devuelve:
        - Un objeto `Client` si el cliente existe, o `None` si no se encuentra el cliente.
    """
    with   get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, telefono, email FROM clientes WHERE id = ?', (client_id,))
        row = cursor.fetchone()
        if row:
            return Client(id=row[0], name=row[1], phone=row[2], email=row[3])
        return None

def create_client(name, phone, email):
    """
    Crea un nuevo cliente en la base de datos.

    Parámetros:
        - name (str): El nombre del cliente.
        - phone (str): El número de teléfono del cliente.
        - email (str): El correo electrónico del cliente.

    Devuelve:
        - El ID del cliente recién creado.
    """
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clientes (nombre, telefono, email) VALUES (?, ?, ?)', (name, phone, email))
        conn.commit()
        return cursor.lastrowid

def update_client(client_id, name, phone, email):
    """
    Actualiza la información de un cliente existente en la base de datos.

    Parámetros:
        - client_id (int): El ID del cliente a actualizar.
        - name (str): El nuevo nombre del cliente.
        - phone (str): El nuevo número de teléfono del cliente.
        - email (str): El nuevo correo electrónico del cliente.
    """
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE clientes SET nombre = ?, telefono = ?, email = ? WHERE id = ?', (name, phone, email, client_id))
        conn.commit()

def delete_client(client_id):
    """
    Elimina un cliente de la base de datos.

    Parámetros:
        - client_id (int): El ID del cliente a eliminar.
    """
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clientes WHERE id = ?', (client_id,))
        conn.commit()
