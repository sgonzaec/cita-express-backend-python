import psycopg2

class RegisterService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def email_exists(self, user):
        # validUserType = ("clients", "sluppiers")[user_type == 2]
        # query = "SELECT COUNT(*) FROM " + validUserType + " WHERE email = %s"
        query = "SELECT COUNT(*) FROM users WHERE email = %s"
        self.cursor.execute(query, (user,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def RegisterUser(self, user, password, user_type):
        
        if self.email_exists(user):
            print("El correo ya existe. No se puede agregar.")
            return -2

        query = "INSERT INTO users (email, password_hash, user_type_id, is_active) VALUES (%s, %s, %s, TRUE)"
        
        try:
            self.cursor.execute(query, (user, password, user_type))
            self.db.commit() 
            return 1
        except psycopg2.Error as err:
            print(f"Error al registrar: {err}")
            return -1
        finally:
            self.cursor.close()
            self.db.close()