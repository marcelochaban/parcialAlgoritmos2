from flask import Blueprint, jsonify, request
from services.position_service import get_all_puestos, get_puesto_by_id, create_puesto, update_puesto, delete_puesto

puesto_routes = Blueprint('puestos', __name__)

@puesto_routes.route('/puestos', methods=['GET'])
def list_puestos():
    """
    Ruta para obtener todos los puestos.

    Método:
        GET

    Respuesta:
        - 200 OK: Devuelve una lista de todos los puestos. Cada puesto es un diccionario con 'id', 'nombre' y 'descripcion'.

    Ejemplo de respuesta:
    [
      {
        "id": 1,
        "nombre": "Gerente",
        "descripcion": "Responsable de la gestión general"
      },
      ...
    ]
    """
    puestos = get_all_puestos()
    puestos_data = [{'id': puesto.id, 'nombre': puesto.name, 'descripcion': puesto.description} for puesto in puestos]
    return jsonify(puestos_data), 200

@puesto_routes.route('/puestos/<int:puesto_id>', methods=['GET'])
def get_puesto(puesto_id):
    """
    Ruta para obtener un puesto por ID.

    Método:
        GET

    Parámetros de la URL:
        - puesto_id (int): El ID del puesto a obtener.

    Respuesta:
        - 200 OK: Devuelve los detalles del puesto.
        - 404 Not Found: Si el puesto no existe.

    Ejemplo de respuesta:
    {
      "id": 1,
      "nombre": "Gerente",
      "descripcion": "Responsable de la gestión general"
    }
    """
    puesto = get_puesto_by_id(puesto_id)
    if puesto:
        return jsonify({'id': puesto.id, 'nombre': puesto.name, 'descripcion': puesto.description}), 200
    return jsonify({'message': 'Puesto no encontrado'}), 404

@puesto_routes.route('/puestos', methods=['POST'])
def add_puesto():
    """
    Ruta para crear un nuevo puesto.

    Método:
        POST

    Cuerpo de la solicitud (JSON):
        {
          "nombre": "Nombre del puesto",
          "descripcion": "Descripción del puesto"
        }

    Respuesta:
        - 201 Created: Devuelve el ID del nuevo puesto creado.
    """
    data = request.json
    puesto_id = create_puesto(data)
    return jsonify({'id': puesto_id}), 201

@puesto_routes.route('/puestos/<int:puesto_id>', methods=['PUT'])
def edit_puesto(puesto_id):
    """
    Ruta para actualizar un puesto existente.

    Método:
        PUT

    Parámetros de la URL:
        - puesto_id (int): El ID del puesto a actualizar.

    Cuerpo de la solicitud (JSON):
        {
          "nombre": "Nuevo nombre",
          "descripcion": "Nueva descripción"
        }

    Respuesta:
        - 200 OK: Confirma que el puesto fue actualizado.
    """
    data = request.json
    update_puesto(puesto_id, data)
    return jsonify({'message': 'Puesto actualizado'}), 200

@puesto_routes.route('/puestos/<int:puesto_id>', methods=['DELETE'])
def remove_puesto(puesto_id):
    """
    Ruta para eliminar un puesto.

    Método:
        DELETE

    Parámetros de la URL:
        - puesto_id (int): El ID del puesto a eliminar.

    Respuesta:
        - 204 No Content: Confirma que el puesto fue eliminado.
    """
    delete_puesto(puesto_id)
    return '', 204
