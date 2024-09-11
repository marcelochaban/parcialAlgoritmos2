from flask import Flask

from db.create import create_tables
from db.drop import delete_products_table
from db.inserts import insert_data
from routes.category_routes import category_routes
from routes.client_routes import client_routes
from routes.position_routes import puesto_routes
from routes.product_routes import product_routes
from routes.employee_routes import employee_routes
from routes.sale_routes import sale_routes


app = Flask(__name__)

# Registrar las rutas (Blueprints)
app.register_blueprint(product_routes)
app.register_blueprint(employee_routes)
app.register_blueprint(sale_routes)

app.register_blueprint(client_routes)
app.register_blueprint(category_routes)
app.register_blueprint(puesto_routes)


if __name__ == '__main__':
    app.run(debug=True)
