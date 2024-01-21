from flask import Flask
from config import Config

# imports
from routes.client_routes import client_routes
from routes.login_routes import login_routes

app = Flask(__name__)
app.config.from_object(Config)

# Registrar las rutas de los clientes
app.register_blueprint(client_routes)
app.register_blueprint(login_routes)

if __name__ == '__main__':
    app.run(debug=True)
