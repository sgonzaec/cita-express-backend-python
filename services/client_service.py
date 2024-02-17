import psycopg2
import base64

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
                # 'image': base64.b64encode(client[9]).decode('utf-8')
            }
            return responseBody
        else:
            return {'error': 'Cliente no encontrado'}

    def update_client(self, data):

        adress = data['adress']
        cp = data['cp']
        email = data['email']
        lastname = data['lastname']
        name = data['name']
        phone = data['phone']

        try:
            self.cursor.execute("UPDATE clients SET name = %s, last_name = %s, phone = %s, adress = %s, cp = %s WHERE email = %s;", (name, lastname, phone, adress, cp, email))
            self.db.commit()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            raise
        finally:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()


    # def save_image(self, image_path, user):
        # try:
        #     with open(image_path, "rb") as image_file:
        #         image_binary = image_file.read()

        #     self.cursor.execute("UPDATE clients SET image = %s WHERE email = %s", (image_binary, user))
        #     responseBody = {
        #         'message': 'La imagen se actualizó correctamente',
        #         'ok': True
        #     }
        # except Exception as e:
        #     responseBody = {
        #         'error': f'Error al actualizar la imagen: {str(e)}',
        #         'ok': False
        #     }
        # return responseBody