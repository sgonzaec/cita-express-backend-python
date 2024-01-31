import psycopg2

class ClientService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def get_client_data(self, dataUser):
        self.cursor.execute("SELECT * FROM clients WHERE email = %s", (dataUser,))
        client = self.cursor.fetchone()
        if client:
            responseBody = {
                'id_client': client[0],
                'name': client[1],
                'lastname': client[2],
                'email': client[3],
                'phone': client[4],
                'city': client[5],
                'country': client[6],
                'adress': client[7],
                'cp': client[8],
                'image': client[9]
            }
            return responseBody
        else:
            return {'error': 'Cliente no encontrado'}
