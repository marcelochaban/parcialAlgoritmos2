# services/category_service.py

import sqlite3
from models.category_model import Category
from db.database import get_db



def get_all_categories():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM categorias')
    categories = cursor.fetchall()
    conn.close()
    return [Category(id=row[0], name=row[1]) for row in categories]

def get_category_by_id(category_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre FROM categorias WHERE id = ?', (category_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Category(id=row[0], name=row[1])
    return None

def create_category(name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO categorias (nombre) VALUES (?)', (name,))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def update_category(category_id, name):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE categorias SET nombre = ? WHERE id = ?', (name, category_id))
    conn.commit()
    conn.close()

def delete_category(category_id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM categorias WHERE id = ?', (category_id,))
    conn.commit()
    conn.close()
