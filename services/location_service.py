import psycopg2

class LocationService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def get_countries(self, country_id=None):
        if country_id is None:
            self.cursor.execute("SELECT * FROM countries")
            countries = self.cursor.fetchall()
            if countries:
                response_body = [{
                    'id': country[0],
                    'name': country[1],
                } for country in countries]
                return response_body
            else:
                return {'error': 'Países no encontrados'}
        else:
            self.cursor.execute("SELECT * FROM countries WHERE id = %s", (country_id,))
            country = self.cursor.fetchone()
            if country:
                response_body = {
                    'id': country[0],
                    'name': country[1],
                }
                return response_body
            else:
                return {'error': 'País no encontrado'}

    def get_states(self, country_id=None):
        self.cursor.execute("SELECT * FROM states WHERE country_location_id = %s", (country_id, ))
        states = self.cursor.fetchall()
        if states:
            response_body = [{
                'id': state[0],
                'country_id': state[1],
                'name': state[2],
            } for state in states]
            return response_body
        else:
            return {'error': 'Departamento/Provincia no encontrados'}