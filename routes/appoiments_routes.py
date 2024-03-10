from flask import Blueprint, jsonify
from services.appoiments_service import LocationService

appoiments_routes = Blueprint('appoiments_routes', __name__)

with open('db_config.env.cfg', 'r') as secret:
    host = secret.readline().strip()
    user = secret.readline().strip()
    password = secret.readline().strip()
    database = secret.readline().strip()

@appoiments_routes.route('/api/appoiments', methods=['GET'])
def getState():
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    appoiments_service = LocationService(db_config)
    appoiments = appoiments_service.get_all_appoiments()

    return jsonify({'appoiments': appoiments})