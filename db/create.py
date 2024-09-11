import sqlite3

def create_tables():
    with sqlite3.connect('inventario.db') as conn:
        cursor = conn.cursor()

        # Crear la tabla de puestos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS puestos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                descripcion TEXT
            )
        ''')

        # Crear la tabla de productos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                categoria TEXT,
                precio REAL NOT NULL,
                stock INTEGER NOT NULL,
                descripcion TEXT
            )
        ''')

        # Crear la tabla de categorías
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            )
        ''')

        # Crear la tabla de empleados
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS empleados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                puesto_id INTEGER,
                salario REAL,
                fecha_contratacion DATE,
                FOREIGN KEY (puesto_id) REFERENCES puestos(id)
            )
        ''')

        # Crear la tabla de clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                telefono TEXT,
                email TEXT
            )
        ''')

        # Crear la tabla de ventas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha DATE NOT NULL,
                total REAL NOT NULL,
                empleado_id INTEGER,
                cliente_id INTEGER,
                FOREIGN KEY (empleado_id) REFERENCES empleados(id),
                FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            )
        ''')

        # Crear la tabla de detalle de ventas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS detalle_ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                venta_id INTEGER,
                producto_id INTEGER,
                cantidad INTEGER,
                precio_unitario REAL,
                FOREIGN KEY (venta_id) REFERENCES ventas(id),
                FOREIGN KEY (producto_id) REFERENCES productos(id)
            )
        ''')

        conn.commit()
