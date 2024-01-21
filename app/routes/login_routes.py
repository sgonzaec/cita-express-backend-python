from flask import Blueprint, jsonify, request
from services.login_service import LoginService

login_routes = Blueprint('login_routes', __name__)

with open('app/db_config.env.cfg', 'r') as secret:
    host = secret.readline().strip()
    user = secret.readline().strip()
    password = secret.readline().strip()
    database = secret.readline().strip()

@login_routes.route('/login', methods=['POST'])
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
    
        login_service = LoginService(db_config)
        
        try:
            loginResponse = login_service.login(dataUser, dataPassword)
            if loginResponse:
                return jsonify({
                    'ok': True,
                    'message' : 'Inicio de sesion Exitoso.'
                }), 200
            else :
                return jsonify({
                    'ok': False,
                    'message' : 'Datos incorrectos.'
                }), 400

        except Exception as e:
            print("Error en la autenticación:", str(e))
            return jsonify({'error': 'Error en la autenticación'}), 500

    else:
        return jsonify({'error': 'Faltan parámetros'}), 400
