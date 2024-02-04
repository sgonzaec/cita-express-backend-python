from flask import Flask
from flask_cors import CORS
from config import Config
from swagger_ui import flask_api_doc

# imports
from routes.client_routes import client_routes
from routes.login_routes import login_routes
from routes.register_routes import register_routes
from routes.location_routes import location_routes

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

flask_api_doc(app, config_path='./swagger.json', url_prefix='/doc', title='API doc')
#Example
# flask_api_doc(app, config_path='./swaggerExample.json', url_prefix='/doc', title='API doc')

# Registrar las rutas de los clientes
app.register_blueprint(client_routes)
app.register_blueprint(login_routes)
app.register_blueprint(register_routes)
app.register_blueprint(location_routes)

if __name__ == '__main__':
    app.run(debug=True)
