from flask import Blueprint, jsonify, request
from services.appoiments_service import AppoimentsService

appoiments_routes = Blueprint('appoiments_routes', __name__)

with open('db_config.env.cfg', 'r') as secret:
    host = secret.readline().strip()
    user = secret.readline().strip()
    password = secret.readline().strip()
    database = secret.readline().strip()

@appoiments_routes.route('/api/appoiments', methods=['GET'])
@appoiments_routes.route('/api/appoiments/<string:filter_email>', methods=['GET'])
def getAppoiments(filter_email=None):
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    filterword = request.args.get('filter')

    appoiments_service = AppoimentsService(db_config)
    
    if filterword is not None:
        appoiments = appoiments_service.get_filtered_appointments(filterword)
    elif filter_email is None:
        appoiments = appoiments_service.get_all_appoiments()
    else:
        appoiments = appoiments_service.get_appoiments(filter_email)

    return jsonify({'appoiments': appoiments})