class Client:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password


class Appointment:
   def __init__(self, id_appointment, id_clients, id_suppliers, services_type, note, country, city):
        self.id_appointment = id_appointment
        self.id_clients = id_clients
        self.id_suppliers = id_suppliers
        self.services_type = services_type
        self.note = note
        self.country = country
        self.city = city

class Categories:
    def __init__(self, id_category, name_category):
        self.id_category = id_category
        self.name_category = name_category

class Countries:
    def __init__(self,id, country_name):
        self.id = id
        self.country_name = country_name

class Services: 
    def __init__(self, id_service, name_service, category_type):
        self.id_service = id_service
        self.name_service = name_service
        self.category_type = category_type

class states:
    def __init__(self, id, country_location_id, state_name):
        self.id = id
        self.country_location_id = country_location_id
        self.state_name = state_name

class 