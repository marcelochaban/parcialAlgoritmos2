from flask import Blueprint, jsonify, request
import services.product_service

product_routes = Blueprint('productos', __name__)


@product_routes.route('/productos', methods=['GET'])
def list_products():
    """
    Ruta para obtener todos los productos.

    Método:
        GET

    Respuesta:
        - 200 OK: Devuelve una lista de todos los productos. Cada producto es un diccionario con 'id', 'nombre', 'categoría', 'precio', 'stock', y 'descripción'.

    Ejemplo de respuesta:
    [
      {
        "id": 1,
        "name": "Cerveza",
        "category": "Bebidas",
        "price": 5.0,
        "stock": 100,
        "description": "Cerveza artesanal"
      },
      ...
    ]
    """
    # Obtiene todos los productos desde el servicio
    products = services.product_service.get_all_products()

    # Prepara los datos de los productos en formato JSON
    products_data = [
        {
            'id': product[0],
            'name': product[1],
            'category': product[2],
            'price': product[3],
            'stock': product[4],
            'description': product[5]
        }
        for product in products
    ]

    # Retorna los datos de los productos con un estado 200 OK
    return jsonify(products_data), 200

@product_routes.route('/productos/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Ruta para obtener un producto por ID.

    Método:
        GET

    Parámetros:
        - product_id (int): El ID del producto a buscar.

    Respuesta:
        - 200 OK: Devuelve los detalles del producto si se encuentra.
        - 404 Not Found: Si el producto no existe.
    """
    product = services.product_service.find_product_by_id(product_id)
    if product:
        product_data = {'id': product.id, 'name': product.name, 'category': product.category, 'price': product.price,
                        'stock': product.stock, 'description': product.description}
        return jsonify(product_data), 200
    return jsonify({'message': 'Producto no encontrado'}), 404

@product_routes.route('/productos', methods=['POST'])
def add_product():
    """
    Ruta para crear un nuevo producto.

    Método:
        POST

    Solicitud:
        - Cuerpo de la solicitud: Un JSON con los datos del producto, por ejemplo:
          {
            "name": "Mojito",
            "category": "Cócteles",
            "price": 7.0,
            "stock": 15,
            "description": "Cóctel refrescante de mojito"
          }

    Respuesta:
        - 201 Created: Devuelve el ID del nuevo producto creado.

    Ejemplo de respuesta:
    {
      "id": 123
    }
    """
    data = request.json
    product_id = services.product_service.create_product(data)
    return jsonify({'id': product_id}), 201


@product_routes.route('/productos/<int:id>', methods=['PUT'])
def edit_product(id):
    """
    Ruta para actualizar un producto existente.

    Método:
        PUT

    Parámetros de la URL:
        - id (int): El ID del producto a actualizar.

    Solicitud:
        - Cuerpo de la solicitud: Un JSON con los datos actualizados del producto, por ejemplo:
          {
            "name": "Mojito",
            "category": "Cócteles",
            "price": 7.5,
            "stock": 20,
            "description": "Cóctel refrescante de mojito con más hierbabuena"
          }

    Respuesta:
        - 200 OK: Devuelve un mensaje confirmando que el producto ha sido actualizado.

    Ejemplo de respuesta:
    {
      "message": "Producto actualizado"
    }
    """
    data = request.json
    services.product_service.update_product(id, data)
    return jsonify({'message': 'Producto actualizado'}), 200


@product_routes.route('/productos/<int:id>', methods=['DELETE'])
def remove_product(id):
    """
    Ruta para eliminar un producto existente.

    Método:
        DELETE

    Parámetros de la URL:
        - id (int): El ID del producto a eliminar.

    Respuesta:
        - 204 No Content: No devuelve contenido en la respuesta.

    Ejemplo de respuesta:
    (Respuesta vacía con estado 204)
    """
    services.product_service.delete_product(id)
    return '', 204
