# routes/category_routes.py

from flask import Blueprint, jsonify, request
from services.category_service import get_all_categories, get_category_by_id, create_category, update_category, delete_category

category_routes = Blueprint('categorias', __name__)

@category_routes.route('/categorias', methods=['GET'])
def list_categories():
    """
    Ruta para obtener todas las categorías.

    Método:
        GET

    Respuesta:
        - 200 OK: Devuelve una lista de todas las categorías. Cada categoría es un diccionario con 'id' y 'nombre'.
    """
    categories = get_all_categories()
    categories_data = [{'id': category.id, 'nombre': category.name} for category in categories]
    return jsonify(categories_data), 200

@category_routes.route('/categorias/<int:category_id>', methods=['GET'])
def get_category(category_id):
    """
    Ruta para obtener una categoría por ID.

    Método:
        GET

    Parámetros:
        - category_id (int): El ID de la categoría a buscar.

    Respuesta:
        - 200 OK: Devuelve los detalles de la categoría si se encuentra.
        - 404 Not Found: Si la categoría no existe.
    """
    category = get_category_by_id(category_id)
    if category:
        category_data = {'id': category.id, 'nombre': category.name}
        return jsonify(category_data), 200
    return jsonify({'message': 'Categoría no encontrada'}), 404

@category_routes.route('/categorias', methods=['POST'])
def add_category():
    """
    Ruta para crear una nueva categoría.

    Método:
        POST

    Solicitud:
        - JSON con el nombre de la categoría.

    Respuesta:
        - 201 Created: Devuelve el ID de la categoría recién creada.
    """
    data = request.json
    category_id = create_category(data['nombre'])
    return jsonify({'id': category_id}), 201

@category_routes.route('/categorias/<int:category_id>', methods=['PUT'])
def edit_category(category_id):
    """
    Ruta para actualizar una categoría existente.

    Método:
        PUT

    Parámetros:
        - category_id (int): El ID de la categoría a actualizar.

    Solicitud:
        - JSON con el nuevo nombre de la categoría.

    Respuesta:
        - 200 OK: Mensaje de confirmación de actualización.
    """
    data = request.json
    update_category(category_id, data['nombre'])
    return jsonify({'message': 'Categoría actualizada'}), 200

@category_routes.route('/categorias/<int:category_id>', methods=['DELETE'])
def remove_category(category_id):
    """
    Ruta para eliminar una categoría.

    Método:
        DELETE

    Parámetros:
        - category_id (int): El ID de la categoría a eliminar.

    Respuesta:
        - 204 No Content: Si la categoría se elimina correctamente.
    """
    delete_category(category_id)
    return '', 204
