class Employee:
    """
    Clase que representa a un empleado.

    Atributos:
        id (int): Identificador único del empleado.
        name (str): Nombre del empleado.
        position_name (str): Nombre del puesto del empleado.
        salary (float): Salario del empleado.
        hire_date (str): Fecha de contratación del empleado.
    """
    def __init__(self, id, name, position_name, salary, hire_date):
        """
        Inicializa una nueva instancia de la clase Employee.

        Parámetros:
            id (int): El identificador único del empleado.
            name (str): El nombre del empleado.
            position_name (str): El nombre del puesto del empleado.
            salary (float): El salario del empleado.
            hire_date (str): La fecha de contratación del empleado.
        """
        self.id = id
        self.name = name
        self.position_name = position_name  # Nombre del puesto en lugar de ID
        self.salary = salary
        self.hire_date = hire_date
