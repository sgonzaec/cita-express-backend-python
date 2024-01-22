from flask import Blueprint, jsonify, request
from services.register_service import RegisterService

register_routes = Blueprint('register_routes', __name__)

with open('app/db_config.env.cfg', 'r') as secret:
    host = secret.readline().strip()
    user = secret.readline().strip()
    password = secret.readline().strip()
    database = secret.readline().strip()

@register_routes.route('/register', methods=['POST'])
def get_sesion():

    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    datos = request.get_json()

    if 'user' in datos and 'password' in datos:
        dataUser = datos['user']
        dataPassword = datos['password']
        dataUserType = datos['user_type']
    
        register_service = RegisterService(db_config)
        
        try:
            registerResponse = register_service.RegisterUser(dataUser, dataPassword, dataUserType)

            if registerResponse == 1:
                return jsonify({
                    'ok': True,
                    'message' : 'Registro Exitoso.'
                }), 200
            elif registerResponse == -1:
                return jsonify({
                    'ok': False,
                    'message' : 'Ha ocurrido un error de conexión.'
                }), 500
            elif registerResponse == -2:
                return jsonify({
                    'ok': False,
                    'message' : 'El usuario ya se encuentra registrado.'
                }), 400

        except Exception as e:
            print("Error en la autenticación:", str(e))
            return jsonify({'error': 'Error en la registrando al usuario'}), 500

    else:
        return jsonify({'error': 'Faltan parámetros'}), 400
