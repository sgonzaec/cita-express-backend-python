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
