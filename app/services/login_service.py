import mysql.connector

class LoginService:
    def __init__(self, db_config):
        self.db = mysql.connector.connect(**db_config)
        self.cursor = self.db.cursor()

    def login(self, user, password):
        query = "SELECT * FROM DataLogin WHERE email = %s"
        self.cursor.execute(query, (user,))
        selected_user = self.cursor.fetchone()

        if selected_user and selected_user[2] == password:
            return True
        else:
            return False
