from flask import Flask
from flask_cors import CORS
from config import Config

# imports
from routes.client_routes import client_routes
from routes.login_routes import login_routes
from routes.register_routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

# Registrar las rutas de los clientes
app.register_blueprint(client_routes)
app.register_blueprint(login_routes)
app.register_blueprint(register_routes)

if __name__ == '__main__':
    app.run(debug=True)
