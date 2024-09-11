class Product:
    """
    Clase que representa un producto.

    Atributos:
        id (int): Identificador único del producto.
        name (str): Nombre del producto.
        category (int): Identificador de la categoría a la que pertenece el producto (relacionado con una tabla de categorías).
        price (float): Precio del producto.
        stock (int): Cantidad de producto disponible en el inventario.
        description (str): Descripción del producto.
    """
    def __init__(self, id, name, category, price, stock, description):
        """
        Inicializa una nueva instancia de la clase Product.

        Parámetros:
            id (int): El identificador único del producto.
            name (str): El nombre del producto.
            category (int): El identificador de la categoría del producto (relacionado con una tabla de categorías).
            price (float): El precio del producto.
            stock (int): La cantidad de productos disponibles en inventario.
            description (str): Una breve descripción del producto.
        """
        self.id = id  # Asigna el ID único del producto.
        self.name = name  # Asigna el nombre del producto.
        self.category = category  # Asigna el ID de la categoría del producto (relacionado con la tabla de categorías).
        self.price = price  # Asigna el precio del producto.
        self.stock = stock  # Asigna la cantidad de productos disponibles en stock.
        self.description = description  # Asigna la descripción del producto.
