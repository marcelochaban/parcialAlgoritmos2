from flask import Blueprint, jsonify, request
from services.employee_service import *

employee_routes = Blueprint('empleados', __name__)


@employee_routes.route('/empleados', methods=['GET'])
def list_employees():
    """
    Ruta para obtener todos los empleados.

    Método:
        GET

    Respuesta:
        - 200 OK: Devuelve una lista de todos los empleados. Cada empleado es un diccionario con 'id', 'nombre', 'puesto', 'salario', y 'fecha_contratacion'.

    Ejemplo de respuesta:
    [
      {
        "id": 1,
        "nombre": "Juan Pérez",
        "puesto": "Gerente",
        "salario": 3000.0,
        "fecha_contratacion": "2023-01-15"
      },
      ...
    ]
    """
    # Obtiene todos los empleados desde el servicio
    employees = get_all_employees()

    # Prepara los datos de los empleados en formato JSON
    employees_data = [
        {
            'id': employee.id,
            'nombre': employee.name,
            'puesto': employee.position_name,
            'salario': employee.salary,
            'fecha_contratacion': employee.hire_date
        }
        for employee in employees
    ]

    # Retorna los datos de los empleados con un estado 200 OK
    return jsonify(employees_data), 200

@employee_routes.route('/empleados/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Ruta para obtener un empleado por ID.

    Método:
        GET

    Parámetros:
        - employee_id (int): El ID del empleado a buscar.

    Respuesta:
        - 200 OK: Devuelve los detalles del empleado si se encuentra.
        - 404 Not Found: Si el empleado no existe.
    """
    employee = find_employee_by_id(employee_id)
    if employee:
        employee_data = {'id': employee.id, 'nombre': employee.name, 'puesto': employee.position_name,
                         'salario': employee.salary, 'fecha_contratacion': employee.hire_date}
        return jsonify(employee_data), 200
    return jsonify({'message': 'Empleado no encontrado'}), 404

@employee_routes.route('/empleados', methods=['POST'])
def add_employee():
    """
    Ruta para crear un nuevo empleado.

    Método:
        POST

    Solicitud:
        - Cuerpo de la solicitud: Un JSON con los datos del empleado, por ejemplo:
          {
            "nombre": "Carlos Gómez",
            "puesto": "Cajero",
            "salario": 2000.0,
            "fecha_contratacion": "2024-09-10"
          }

    Respuesta:
        - 201 Created: Devuelve el ID del nuevo empleado creado.

    Ejemplo de respuesta:
    {
      "id": 123
    }
    """
    data = request.json
    employee_id = create_employee(data)
    return jsonify({'id': employee_id}), 201


@employee_routes.route('/empleados/<int:id>', methods=['PUT'])
def edit_employee(id):
    """
    Ruta para actualizar un empleado existente.

    Método:
        PUT

    Parámetros de la URL:
        - id (int): El ID del empleado a actualizar.

    Solicitud:
        - Cuerpo de la solicitud: Un JSON con los datos actualizados del empleado, por ejemplo:
          {
            "nombre": "Carlos Gómez",
            "puesto": "Supervisor",
            "salario": 2200.0,
            "fecha_contratacion": "2024-09-10"
          }

    Respuesta:
        - 200 OK: Devuelve un mensaje confirmando que el empleado ha sido actualizado.

    Ejemplo de respuesta:
    {
      "message": "Empleado actualizado"
    }
    """
    data = request.json
    update_employee(id, data)
    return jsonify({'message': 'Empleado actualizado'}), 200


@employee_routes.route('/empleados/<int:id>', methods=['DELETE'])
def remove_employee(id):
    """
    Ruta para eliminar un empleado existente.

    Método:
        DELETE

    Parámetros de la URL:
        - id (int): El ID del empleado a eliminar.

    Respuesta:
        - 204 No Content: No devuelve contenido en la respuesta.

    Ejemplo de respuesta:
    (Respuesta vacía con estado 204)
    """
    delete_employee(id)
    return '', 204
