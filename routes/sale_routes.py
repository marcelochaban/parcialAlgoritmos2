from flask import Blueprint, jsonify, request
from services.sale_service import get_all_sales, create_sale, get_sale_with_details

sale_routes = Blueprint('ventas', __name__)

@sale_routes.route('/ventas/<int:sale_id>', methods=['GET'])
def get_sale_details(sale_id):
    """
    Ruta para obtener los detalles de una venta específica.

    Método:
        GET

    Parámetros de la URL:
        - sale_id (int): El ID de la venta para obtener detalles.

    Respuesta:
        - 200 OK: Devuelve un diccionario con los detalles de la venta.
        - 404 Not Found: Si no se encuentra la venta.

    Ejemplo de respuesta:
    {
      "id": 1,
      "date": "2024-09-10",
      "total": 150.0,
      "employee_id": 3,
      "client_id": 5,
      "details": [
        {
          "product_id": 2,
          "quantity": 3,
          "price": 8.0
        },
        ...
      ]
    }
    """
    sale = get_sale_with_details(sale_id)
    if sale:
        return jsonify(sale), 200
    return jsonify({'message': 'Sale not found'}), 404

@sale_routes.route('/ventas', methods=['GET'])
def list_sales():
    """
    Ruta para obtener una lista de todas las ventas.

    Método:
        GET

    Respuesta:
        - 200 OK: Devuelve una lista de todas las ventas. Cada venta es un diccionario con 'id', 'date', 'total', 'employee_id', y 'client_id'.

    Ejemplo de respuesta:
    [
      {
        "id": 1,
        "date": "2024-09-10",
        "total": 150.0,
        "employee_id": 3,
        "client_id": 5
      },
      ...
    ]
    """
    sales = get_all_sales()
    return jsonify(sales), 200

@sale_routes.route('/ventas', methods=['POST'])
def add_sale():
    """
    Ruta para crear una nueva venta.

    Método:
        POST

    Solicitud:
        - Cuerpo de la solicitud: Un JSON con los detalles de la venta, por ejemplo:
          {
            "date": "2024-09-10",
            "total": 150.0,
            "employee_id": 3,
            "client_id": 5,
            "details": [
              {
                "product_id": 2,
                "quantity": 3,
                "price": 8.0
              }
            ]
          }

    Respuesta:
        - 201 Created: Devuelve el ID de la nueva venta creada.

    Ejemplo de respuesta:
    {
      "id": 123
    }
    """
    data = request.json
    sale_id = create_sale(data)
    return jsonify({'id': sale_id}), 201
