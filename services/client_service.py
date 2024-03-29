import psycopg2
import os
import base64

class ClientService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def get_client_data(self, dataUser):
        query = ("SELECT clients.*, s.state_name AS city_name, co.country_name AS country_name FROM clients"
                " LEFT JOIN states s ON clients.city = s.id::varchar"
                " LEFT JOIN countries co ON s.country_location_id = co.id"
                " WHERE clients.email = %s")

        self.cursor.execute(query, (dataUser,))
        client = self.cursor.fetchone()
        if client:
            id_client, name, lastname, email, phone, city, country, address, cp, image_bytes, city_name, country_name = client
            image_base64 = base64.b64encode(image_bytes).decode('utf-8') if image_bytes else None

            responseBody = {
                'id_client': id_client,
                'name': name,
                'lastname': lastname,
                'email': email,
                'phone': phone,
                'city': city_name,
                'country': country_name,
                'address': address,
                'cp': cp,
                'image': image_base64
            }
            
            return responseBody
        else:
            return {'error': 'Cliente no encontrado'}

    def update_client(self, data):

        address = data['address']
        cp = data['cp']
        email = data['email']
        lastname = data['lastname']
        country = data['country']
        city = data['city']
        name = data['name']
        phone = data['phone']

        try:
            self.cursor.execute("UPDATE clients SET name = %s, last_name = %s, phone = %s, country = %s, address = %s, state = %s, cp = %s WHERE email = %s;", (name, lastname, phone, country, city, address, cp, email))
            self.db.commit()
        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")
            raise
        finally:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()

    def save_image(self, image_data, user_email, ruta_guardado):
        try:
            query = "UPDATE clients SET image = %s WHERE email = %s"
            self.cursor.execute(query, (psycopg2.Binary(image_data), user_email))
            self.db.commit()
            os.remove(ruta_guardado)
            return {'message': 'La imagen se actualizó correctamente', 'ok': True}
        except Exception as e:
            return {'error': f'Error al actualizar la imagen: {str(e)}', 'ok': False}
        finally:
            if self.cursor:
                self.cursor.close()
            if self.db:
                self.db.close()
