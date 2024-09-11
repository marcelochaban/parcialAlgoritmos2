from db.database import get_db
from models.position_model import Position

def get_all_puestos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, descripcion FROM puestos')
    puestos = cursor.fetchall()
    return [Position(id=row[0], name=row[1], description=row[2]) for row in puestos]

def get_puesto_by_id(puesto_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, descripcion FROM puestos WHERE id = ?', (puesto_id,))
    row = cursor.fetchone()
    if row:
        return Position(id=row[0], name=row[1], description=row[2])
    return None

def create_puesto(data):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO puestos (nombre, descripcion) VALUES (?, ?)',
                   (data['nombre'], data['descripcion']))
    conn.commit()
    return cursor.lastrowid

def update_puesto(puesto_id, data):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE puestos SET nombre = ?, descripcion = ? WHERE id = ?',
                   (data['nombre'], data['descripcion'], puesto_id))
    conn.commit()

def delete_puesto(puesto_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM puestos WHERE id = ?', (puesto_id,))
    conn.commit()
