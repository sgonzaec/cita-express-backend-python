# app/services/client_service.py
import mysql.connector

class ClientService:
    def __init__(self, db_config):
        self.db = mysql.connector.connect(**db_config)
        self.cursor = self.db.cursor()

    def get_all_clients(self):
        self.cursor.execute("SELECT * FROM Clients")
        clients = self.cursor.fetchall()
        return clients
