# app/routes/client_routes.py
from flask import Blueprint, jsonify
from services.client_service import ClientService

client_routes = Blueprint('client_routes', __name__)

@client_routes.route('/api/clients', methods=['GET'])
def get_clients():
    db_config = {
        'host': 'localhost',
        'user': 'admincitaexpress',
        'password': 'C1ta3xpress*.',
        'database': 'citaexpress'
    }
    client_service = ClientService(db_config)
    clients = client_service.get_all_clients()
    return jsonify({'clients': clients})
