import jwt
import psycopg2

class LoginService:
    
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def login(self, user, password):
        query = "SELECT * FROM users WHERE email = %s"

        try:
            self.cursor.execute(query, (user,))
            selected_user = self.cursor.fetchone()

            if selected_user and selected_user[2] == password:
                token = jwt.encode({'username': username, 'exp': datetime.utcnow() + timedelta(days=1)}, app.config['C1t4Xpr3ss*.*'], algorithm='HS256')
                return token
            else:
                return False
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            raise
        finally:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()
            
