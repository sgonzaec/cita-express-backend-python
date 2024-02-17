from flask import Blueprint, jsonify, request
from services.client_service import ClientService

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
        print(updateClientReasponse)

    except Exception as e:
        print("Error en la autenticación:", str(e))
        return jsonify({'error': 'Error en la autenticacion'}), 500

    else:
        return jsonify({'success': 'Cliente actualizado exitosamente'}), 200



# @client_routes.route('/api/clients/updateImage', methods=['POST'])
# def updateImage():
    # db_config = {
    #     'host': host,
    #     'user': user,
    #     'password': password,
    #     'database': database
    # }

    # data = request.get_json()

    # user_email = data['user']
    # image = data['image']

    # if not user_email or not image:
    #     return jsonify({'error': 'Se requiere el correo electrónico del usuario y la imagen en formato Base64'}), 400

    # client_service = ClientService(db_config)
    # print(image, user_email)
    # response = client_service.save_image(image, user_email) 
    # return jsonify({'response': response})
