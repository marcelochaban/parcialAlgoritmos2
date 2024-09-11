from models.product_model import Product
from db.database import get_db

def get_all_products():
    """
    Obtiene todos los productos desde la base de datos.

    Devuelve:
        - Una lista de objetos `Product`, donde cada objeto representa un producto en la base de datos.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, nombre, categoria, precio, stock, descripcion FROM productos')
    products = cursor.fetchall()

    # Convierte los resultados en una lista de objetos Product
    product_list = [Product(id=row[0], name=row[1], category=row[2], price=row[3], stock=row[4], description=row[5]) for row in products]

    conn.close()  # Cierra la conexión a la base de datos
    return product_list

def find_product_by_id(product_id):
    """
    Busca un producto por su ID.

    Parámetros:
        - product_id (int): El ID del producto a buscar.

    Devuelve:
        - Un objeto Product si se encuentra el producto, de lo contrario, `None`.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos WHERE id = ?', (product_id,))
    row = cursor.fetchone()

    if row:
        return Product(id=row[0], name=row[1], category=row[2], price=row[3], stock=row[4], description=row[5])
    return None

def create_product(data):
    """
    Crea un nuevo producto en la base de datos.

    Parámetros:
        - data (dict): Un diccionario con los detalles del producto, incluyendo 'nombre', 'categoria', 'precio', 'stock', y 'descripcion'.

    Devuelve:
        - El ID del producto recién creado.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO productos (nombre, categoria, precio, stock, descripcion) VALUES (?, ?, ?, ?, ?)',
                   (data['nombre'], data['categoria'], data['precio'], data['stock'], data['descripcion']))
    conn.commit()

    return cursor.lastrowid

def update_product(product_id, data):
    """
    Actualiza la información de un producto existente en la base de datos.

    Parámetros:
        - product_id (int): El ID del producto a actualizar.
        - data (dict): Un diccionario con los nuevos detalles del producto, incluyendo 'nombre', 'categoria', 'precio', 'stock', y 'descripcion'.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE productos SET nombre = ?, categoria = ?, precio = ?, stock = ?, descripcion = ? WHERE id = ?',
                   (data['nombre'], data['categoria'], data['precio'], data['stock'], data['descripcion'], product_id))
    conn.commit()

def delete_product(product_id):
    """
    Elimina un producto de la base de datos.

    Parámetros:
        - product_id (int): El ID del producto a eliminar.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM productos WHERE id = ?', (product_id,))
    conn.commit()
