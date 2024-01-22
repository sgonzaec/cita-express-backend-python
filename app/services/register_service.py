import mysql.connector

class RegisterService:
    def __init__(self, db_config):
        self.db = mysql.connector.connect(**db_config)
        self.cursor = self.db.cursor()

    def email_exists(self, user):
        query = "SELECT COUNT(*) FROM DataLogin WHERE email = %s"
        self.cursor.execute(query, (user,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def RegisterUser(self, user, password, user_type):
        
        if self.email_exists(user):
            print("El correo ya existe. No se puede agregar.")
            return -2

        query = "INSERT INTO DataLogin (email, password, user_type, is_active) VALUES (%s, %s, %s, TRUE)"
        
        try:
            self.cursor.execute(query, (user, password, int(user_type)))
            self.db.commit() 
            return 1
        except mysql.connector.Error as err:
            print(f"Error al registrar: {err}")
            return -1
        finally:
            self.cursor.close()
            self.db.close()