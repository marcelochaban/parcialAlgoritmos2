
class Config:
    """
    Clase de configuración para la aplicación.

    Atributos:
        DEBUG (bool): Activa el modo de depuración (True permite ver los errores en el navegador).
        DATABASE (str): Nombre de la base de datos que se utilizará en la aplicación.
    """
    DEBUG = True  # Habilita el modo de depuración para ver mensajes de error y depurar problemas.
    DATABASE = 'inventario.db'  # Define el nombre de la base de datos que será utilizada.

# Crea una instancia de la clase de configuración para acceder a las configuraciones.
config = Config()