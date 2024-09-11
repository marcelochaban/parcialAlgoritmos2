from db.database import get_db
from models.employee_model import Employee

def get_all_employees():
    """
    Obtiene todos los empleados desde la base de datos con detalles del puesto.

    Devuelve:
        - Una lista de objetos `Employee`, donde cada objeto representa un empleado en la base de datos.
    """
    conn = get_db()  # Obtiene la conexión a la base de datos
    cursor = conn.cursor()
    query = '''
        SELECT e.id, e.nombre, p.nombre AS puesto, e.salario, e.fecha_contratacion
        FROM empleados e
        JOIN puestos p ON e.puesto_id = p.id
    '''
    cursor.execute(query)
    employees = cursor.fetchall()

    # Convierte los resultados en una lista de objetos Employee
    employee_list = [Employee(id=row[0], name=row[1], position_name=row[2], salary=row[3], hire_date=row[4]) for row in employees]

    conn.close()  # Cierra la conexión a la base de datos
    return employee_list

def find_employee_by_id(employee_id):
    """
    Busca un empleado por su ID.

    Parámetros:
        - employee_id (int): El ID del empleado a buscar.

    Devuelve:
        - Un objeto Employee si se encuentra el empleado, de lo contrario, `None`.
    """
    conn = get_db()
    cursor = conn.cursor()
    query = '''
        SELECT e.id, e.nombre, p.nombre AS puesto, e.salario, e.fecha_contratacion
        FROM empleados e
        JOIN puestos p ON e.puesto_id = p.id
        WHERE e.id = ?
    '''
    cursor.execute(query, (employee_id,))
    row = cursor.fetchone()

    if row:
        return Employee(id=row[0], name=row[1], position_name=row[2], salary=row[3], hire_date=row[4])
    return None

def create_employee(data):
    """
    Crea un nuevo empleado en la base de datos.

    Parámetros:
        - data (dict): Un diccionario con los detalles del empleado, incluyendo 'nombre', 'puesto_id', 'salario', y 'fecha_contratacion'.

    Devuelve:
        - El ID del empleado recién creado.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO empleados (nombre, puesto_id, salario, fecha_contratacion) VALUES (?, ?, ?, ?)',
                   (data['nombre'], data['puesto_id'], data['salario'], data['fecha_contratacion']))
    conn.commit()

    return cursor.lastrowid

def update_employee(employee_id, data):
    """
    Actualiza la información de un empleado existente en la base de datos.

    Parámetros:
        - employee_id (int): El ID del empleado a actualizar.
        - data (dict): Un diccionario con los nuevos detalles del empleado, incluyendo 'nombre', 'puesto_id', 'salario', y 'fecha_contratacion'.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE empleados SET nombre = ?, puesto_id = ?, salario = ?, fecha_contratacion = ? WHERE id = ?',
                   (data['nombre'], data['puesto_id'], data['salario'], data['fecha_contratacion'], employee_id))
    conn.commit()

def delete_employee(employee_id):
    """
    Elimina un empleado de la base de datos.

    Parámetros:
        - employee_id (int): El ID del empleado a eliminar.
    """
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM empleados WHERE id = ?', (employee_id,))
    conn.commit()
