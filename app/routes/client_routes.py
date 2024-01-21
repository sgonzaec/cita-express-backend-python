from flask import Blueprint, jsonify
from services.client_service import ClientService

client_routes = Blueprint('client_routes', __name__)


with open('app/db_config.env.cfg', 'r') as secreto:
    host = secreto.readline().strip()
    user = secreto.readline().strip()
    password = secreto.readline().strip()
    database = secreto.readline().strip()

@client_routes.route('/api/clients', methods=['GET'])
def get_clients():
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }
    client_service = ClientService(db_config)
    clients = client_service.get_all_clients()
    return jsonify({'clients': clients})
