class Client:
    """
    Clase que representa a un cliente.

    Atributos:
        id (int): Identificador único del cliente.
        name (str): Nombre del cliente.
        phone (str): Número de teléfono del cliente.
        email (str): Correo electrónico del cliente.
    """
    def __init__(self, id, name, phone, email):
        """
        Inicializa una nueva instancia de la clase Client.

        Parámetros:
            id (int): El identificador único del cliente.
            name (str): El nombre del cliente.
            phone (str): El número de teléfono del cliente.
            email (str): El correo electrónico del cliente.
        """
        self.id = id  # Asigna el ID del cliente.
        self.name = name  # Asigna el nombre del cliente.
        self.phone = phone  # Asigna el número de teléfono del cliente.
        self.email = email  # Asigna el correo electrónico del cliente.
