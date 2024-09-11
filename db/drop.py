from db.database import get_db

def delete_products_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS products')
    conn.commit()