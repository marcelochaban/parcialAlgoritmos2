class Sale:
    """
    Clase que representa una venta.

    Atributos:
        id (int): Identificador único de la venta.
        date (str): Fecha en que se realizó la venta (formato esperado: 'YYYY-MM-DD').
        total (float): Monto total de la venta.
        employee_id (int): Identificador del empleado que realizó la venta (relacionado con una tabla de empleados).
        client_id (int): Identificador del cliente que realizó la compra (relacionado con una tabla de clientes).
    """
    def __init__(self, id, date, total, employee_id, client_id):
        """
        Inicializa una nueva instancia de la clase Sale.

        Parámetros:
            id (int): El identificador único de la venta.
            date (str): La fecha en que se realizó la venta (formato esperado: 'YYYY-MM-DD').
            total (float): El monto total de la venta.
            employee_id (int): El identificador del empleado que realizó la venta (relacionado con otra tabla).
            client_id (int): El identificador del cliente que realizó la compra (relacionado con otra tabla).
        """
        self.id = id  # Asigna el ID único de la venta.
        self.date = date  # Asigna la fecha de la venta.
        self.total = total  # Asigna el monto total de la venta.
        self.employee_id = employee_id  # Asigna el ID del empleado que realizó la venta (relacionado con una tabla de empleados).
        self.client_id = client_id  # Asigna el ID del cliente que realizó la compra (relacionado con una tabla de clientes).
