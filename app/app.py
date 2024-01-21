# app/app.py
from flask import Flask
from routes.client_routes import client_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Registrar las rutas de los clientes
app.register_blueprint(client_routes)

if __name__ == '__main__':
    app.run(debug=True)
