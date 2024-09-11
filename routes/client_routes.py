from flask import Blueprint, jsonify, request
from services.client_service import get_all_clients, get_client_by_id, create_client, update_client, delete_client

# Crea un blueprint para las rutas de clientes
client_routes = Blueprint('clients', __name__)


# Obtener todos los clientes
@client_routes.route('/clientes', methods=['GET'])
def get_clients():
    # Obtiene todos los clientes desde el servicio
    clients = get_all_clients()
    # Prepara los datos de los clientes en formato JSON
    clients_data = [{'id': client.id, 'nombre': client.name, 'telefono': client.phone, 'email': client.email} for client
                    in clients]
    # Retorna los datos de los clientes con un estado 200 OK
    return jsonify(clients_data), 200


# Obtener un cliente por ID
@client_routes.route('/clientes/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """
    Ruta para obtener un cliente específico por su ID.

    Parámetros:
        - client_id (int): ID del cliente a obtener.

    Método:
        GET

    Respuesta:
        - 200 OK: Devuelve los datos del cliente como un diccionario con 'id', 'name', 'phone', y 'email'.
        - 404 Not Found: Si el cliente no existe, devuelve un mensaje de error.

    Ejemplo de respuesta (200 OK):
    {
      "id": 1,
      "name": "María Rodríguez",
      "phone": "555-1234",
      "email": "maria@example.com"
    }
    Ejemplo de respuesta (404 Not Found):
    {
      "message": "Client not found"
    }
    """
    # Obtiene el cliente por ID desde el servicio
    client = get_client_by_id(client_id)
    if client:
        # Prepara los datos del cliente en formato JSON
        client_data = {'id': client.id, 'name': client.name, 'phone': client.phone, 'email': client.email}
        # Retorna los datos del cliente con un estado 200 OK
        return jsonify(client_data), 200
    # Retorna un mensaje de error si el cliente no se encuentra con un estado 404 Not Found
    return jsonify({'message': 'Client not found'}), 404


# Crear un nuevo cliente
@client_routes.route('/clientes', methods=['POST'])
def add_client():
    """
    Ruta para crear un nuevo cliente.

    Método:
        POST

    Cuerpo de la solicitud:
        - name (str): Nombre del cliente.
        - phone (str): Número de teléfono del cliente.
        - email (str): Correo electrónico del cliente.

    Respuesta:
        - 201 Created: Devuelve un mensaje de éxito y el ID del cliente creado.

    Ejemplo de respuesta:
    {
      "message": "Client created",
      "client_id": 1
    }
    """
    # Obtiene los datos del nuevo cliente desde la solicitud
    data = request.get_json()
    # Crea el nuevo cliente y obtiene su ID
    client_id = create_client(data['name'], data['phone'], data['email'])
    # Retorna un mensaje de éxito con el ID del cliente creado
    return jsonify({'message': 'Client created', 'client_id': client_id}), 201


# Actualizar un cliente existente
@client_routes.route('/clientes/<int:client_id>', methods=['PUT'])
def edit_client(client_id):
    """
    Ruta para actualizar los datos de un cliente existente.

    Parámetros:
        - client_id (int): ID del cliente a actualizar.

    Método:
        PUT

    Cuerpo de la solicitud:
        - name (str): Nombre del cliente.
        - phone (str): Número de teléfono del cliente.
        - email (str): Correo electrónico del cliente.

    Respuesta:
        - 200 OK: Devuelve un mensaje de éxito si la actualización fue exitosa.
    """
    # Obtiene los datos actualizados del cliente desde la solicitud
    data = request.get_json()
    # Actualiza el cliente con los nuevos datos
    update_client(client_id, data['name'], data['phone'], data['email'])
    # Retorna un mensaje de éxito con un estado 200 OK
    return jsonify({'message': 'Client updated'}), 200


# Eliminar un cliente
@client_routes.route('/clientes/<int:client_id>', methods=['DELETE'])
def remove_client(client_id):
    """
    Ruta para eliminar un cliente por su ID.

    Parámetros:
        - client_id (int): ID del cliente a eliminar.

    Método:
        DELETE

    Respuesta:
        - 200 OK: Devuelve un mensaje de éxito si la eliminación fue exitosa.
    """
    # Elimina el cliente con el ID especificado
    delete_client(client_id)
    # Retorna un mensaje de éxito con un estado 200 OK
    return jsonify({'message': 'Client deleted'}), 200
