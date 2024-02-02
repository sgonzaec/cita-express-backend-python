from flask import Blueprint, jsonify, request
from services.location_service import LocationService

location_routes = Blueprint('location_routes', __name__)

with open('db_config.env.cfg', 'r') as secret:
    host = secret.readline().strip()
    user = secret.readline().strip()
    password = secret.readline().strip()
    database = secret.readline().strip()

@location_routes.route('/countries', methods=['GET'])
@location_routes.route('/countries/<int:country_id>', methods=['GET'])
def get_countries(country_id=None):
    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    location_service = LocationService(db_config)

    if country_id is None:
        countries = location_service.get_countries()
    else:
        countries = location_service.get_countries(country_id)

    return jsonify({'countries': countries})
