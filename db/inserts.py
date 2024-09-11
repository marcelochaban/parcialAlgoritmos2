import sqlite3

def insert_data():
    with sqlite3.connect('inventario.db') as conn:
        cursor = conn.cursor()

        # Verificar si los puestos ya existen
        cursor.execute("SELECT COUNT(*) FROM puestos")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO puestos (nombre, descripcion) VALUES
                ('Bartender', 'Encargado de preparar y servir bebidas.'),
                ('Cocinero', 'Encargado de preparar los alimentos.'),
                ('Mesero', 'Encargado de atender a los clientes en las mesas.')
            ''')

        # Verificar si las categorías ya existen
        cursor.execute("SELECT COUNT(*) FROM categorias")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO categorias (nombre) VALUES
                ('Bebidas'),
                ('Comidas'),
                ('Aperitivos'),
                ('Postres'),
                ('Cócteles')
            ''')

        # Verificar si los productos ya existen
        cursor.execute("SELECT COUNT(*) FROM productos")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO productos (nombre, categoria, precio, stock, descripcion) VALUES
                ('Cerveza', 'Bebidas', 5.00, 100, 'Cerveza artesanal'),
                ('Hamburguesa', 'Comidas', 8.00, 50, 'Hamburguesa con queso'),
                ('Nachos', 'Aperitivos', 6.00, 30, 'Nachos con queso y guacamole'),
                ('Tarta de Chocolate', 'Postres', 4.50, 20, 'Tarta de chocolate casera'),
                ('Mojito', 'Cócteles', 7.00, 15, 'Cóctel refrescante de mojito')
            ''')

        # Verificar si los empleados ya existen
        cursor.execute("SELECT COUNT(*) FROM empleados")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO empleados (nombre, puesto_id, salario, fecha_contratacion) VALUES
                ('Juan Pérez', 1, 1500.00, '2024-01-15'),
                ('Ana García', 2, 1600.00, '2024-02-10'),
                ('Carlos López', 3, 1400.00, '2024-03-05')
            ''')

        # Verificar si los clientes ya existen
        cursor.execute("SELECT COUNT(*) FROM clientes")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO clientes (nombre, telefono, email) VALUES
                ('María Rodríguez', '555-1234', 'maria@example.com'),
                ('Luis Fernández', '555-5678', 'luis@example.com'),
                ('Laura Martínez', '555-8765', 'laura@example.com')
            ''')

        # Verificar si las ventas ya existen
        cursor.execute("SELECT COUNT(*) FROM ventas")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO ventas (fecha, total, empleado_id, cliente_id) VALUES
                ('2024-09-09', 19.00, 1, 1),
                ('2024-09-10', 14.00, 2, 2)
            ''')

        # Verificar si los detalles de ventas ya existen
        cursor.execute("SELECT COUNT(*) FROM detalle_ventas")
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
                INSERT INTO detalle_ventas (venta_id, producto_id, cantidad, precio_unitario) VALUES
                (1, 1, 2, 5.00),  -- 2 cervezas
                (1, 2, 1, 8.00),  -- 1 hamburguesa
                (2, 3, 2, 6.00)   -- 2 nachos
            ''')

        conn.commit()

