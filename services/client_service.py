import psycopg2

class ClientService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def get_all_clients(self):
        self.cursor.execute("SELECT * FROM clients")
        clients = self.cursor.fetchall()
        return clients
