from db.database import get_db

def get_sale_with_details(sale_id):
    """
    Obtiene los detalles de una venta específica, incluyendo la información básica de la venta y los detalles de los productos vendidos.

    Parámetros:
        - sale_id (int): El ID de la venta a obtener.

    Devuelve:
        - Un diccionario con la información de la venta, incluyendo:
            - 'id': ID de la venta.
            - 'date': Fecha de la venta.
            - 'total': Monto total de la venta.
            - 'client': Nombre del cliente.
            - 'employee': Nombre del empleado que realizó la venta.
            - 'details': Una lista de diccionarios con los detalles de los productos vendidos (nombre, cantidad, precio unitario).
        - `None` si la venta no se encuentra.
    """
    conn = get_db()
    cursor = conn.cursor()

    # Obtener la venta básica
    cursor.execute('''
        SELECT v.id, v.fecha, v.total, c.nombre AS cliente, e.nombre AS empleado
        FROM ventas v
        JOIN clientes c ON v.cliente_id = c.id
        JOIN empleados e ON v.empleado_id = e.id
        WHERE v.id = ?
    ''', (sale_id,))
    sale = cursor.fetchone()

    if not sale:
        return None

    # Obtener los detalles de la venta (productos, cantidad, precio)
    cursor.execute('''
        SELECT p.nombre, dv.cantidad, dv.precio_unitario
        FROM detalle_ventas dv
        JOIN productos p ON dv.producto_id = p.id
        WHERE dv.venta_id = ?
    ''', (sale_id,))
    details = cursor.fetchall()

    return {
        'id': sale[0],
        'date': sale[1],
        'total': sale[2],
        'client': sale[3],
        'employee': sale[4],
        'details': [{'product': row[0], 'quantity': row[1], 'unit_price': row[2]} for row in details]
    }

def get_all_sales():
    """
    Obtiene todas las ventas desde la base de datos.

    Devuelve:
        - Una lista de tuplas, donde cada tupla representa una venta. Cada tupla contiene los campos de la tabla de ventas.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ventas')
    sales = cursor.fetchall()
    return sales

def create_sale(data):
    """
    Crea una nueva venta en la base de datos.

    Parámetros:
        - data (dict): Un diccionario con los detalles de la venta, incluyendo 'fecha', 'total', 'empleado_id', y 'cliente_id'.

    Devuelve:
        - El ID de la venta recién creada.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ventas (fecha, total, empleado_id, cliente_id) VALUES (?, ?, ?, ?)',
                   (data['fecha'], data['total'], data['empleado_id'], data['cliente_id']))
    conn.commit()
    return cursor.lastrowid
