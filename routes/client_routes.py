from flask import Blueprint, jsonify, request
from services.client_service import ClientService
import base64

client_routes = Blueprint('client_routes', __name__)

with open('db_config.env.cfg', 'r') as secret:
    host = secret.readline().strip()
    user = secret.readline().strip()
    password = secret.readline().strip()
    database = secret.readline().strip()

@client_routes.route('/api/clients', methods=['GET'])
def get_clients():
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    dataUser = request.args.get('user')

    client_service = ClientService(db_config)
    client = client_service.get_client_data(dataUser)
    return jsonify({'client': client})

@client_routes.route('/api/clients/updateUserData', methods=['POST'])
def update_client():
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }
    
    data = request.get_json()

    client_service = ClientService(db_config)
    try:
        updateClientReasponse = client_service.update_client(data)

    except Exception as e:
        print("Error en la autenticación:", str(e))
        return jsonify({'error': 'Error en la autenticacion'}), 500

    else:
        return jsonify({'success': 'Cliente actualizado exitosamente'}), 200

@client_routes.route('/api/clients/updateImage', methods=['POST'])
def updateImage():
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    user_email = request.form.get('user')
    image_file = request.files['image']

    client_service = ClientService(db_config)

    if not user_email or not image_file:
        return jsonify({'error': 'Se requiere el correo electrónico del usuario y la imagen en formato correcto'}), 400

    if image_file:
        ruta_guardado = f"./tempFiles/{image_file.filename}"
        image_file.save(ruta_guardado)

        with open(ruta_guardado, "rb") as file:
            archivo = file.read()

    response = client_service.save_image(archivo, user_email, ruta_guardado) 
    return jsonify({'response': response})
