import psycopg2

class AppoimentsService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

    def get_appoiments(self, email):
        self.cursor.execute("SELECT "
                        "    a.id_appointment, "
                        "    c.name AS client_name, "
                        "    CONCAT(s.name, ' ', s.last_name) AS supplier_name, "
                        "    s.phone AS supplier_phone, "
                        "    s.cp AS supplier_cp, "
                        "    srv.name_service AS service_name, "
                        "    a.note, "
                        "    co.country_name AS country_name, "
                        "    st.state_name AS city_name "
                        "FROM "
                        "    public.appointments a "
                        "JOIN public.clients c ON a.id_clients = c.id_client "
                        "JOIN public.suppliers s ON a.id_suppliers = s.id_supplier "
                        "JOIN public.services srv ON a.services_type = srv.id_service "
                        "LEFT JOIN public.countries co ON a.country = co.id "
                        "LEFT JOIN public.states st ON a.city = st.id "
                        "WHERE c.email = %s;", (email,))

        appointments = self.cursor.fetchall()
        if appointments:
            response_body = [{
                'id_appointment': appointment[0],
                'client_name': appointment[1],
                'supplier_name': appointment[2],
                'supplier_phone': appointment[3],
                'supplier_cp': appointment[4],
                'service_type': appointment[5],
                'note': appointment[6],
                'country': appointment[7],
                'city': appointment[8],
            } for appointment in appointments]
            return response_body
        else:
            return {'error': 'No se encontraron citas para este correo electrónico'}
        
    def get_filtered_appointments(self, filterword):
        self.cursor.execute(
            'SELECT ga.appointment_id, ga.appointment_date_published, ga.appointment_description, s."name" AS supplier_name '
            'FROM public.generalappointments ga '
            'LEFT JOIN public.suppliers s ON ga.id_supplier = s.id_supplier '
            'WHERE ga.appointment_description ILIKE %s', ('%' + filterword + '%',)
        )

        filtered_data = self.cursor.fetchall()

        if filtered_data:
            response_body = []
            for data in filtered_data:
                response_body.append({
                    'id_appointment': data[0],
                    'appointment_date_published': data[1],
                    'appointment_description': data[2],
                    'supplier_name': data[3]
                })
            return response_body
        else:
            return {'error': 'No se encontraron citas con esta palabra.'}

    def get_all_appoiments(self, ):
        self.cursor.execute("SELECT "
                            "    a.id_appointment, "
                            "    c.name AS client_name, "
                            "    CONCAT(s.name, ' ', s.last_name) AS supplier_name, "
                            "    s.phone AS supplier_phone, "
                            "    s.cp AS supplier_cp, "
                            "    srv.name_service AS service_name, "
                            "    a.note, "
                            "    co.country_name AS country_name, "
                            "    st.state_name AS city_name "
                            "FROM "
                            "    public.appointments a "
                            "JOIN public.clients c ON a.id_clients = c.id_client "
                            "JOIN public.suppliers s ON a.id_suppliers = s.id_supplier "
                            "JOIN public.services srv ON a.services_type = srv.id_service "
                            "LEFT JOIN public.countries co ON a.country = co.id "
                            "LEFT JOIN public.states st ON a.city = st.id;")

        appoiments = self.cursor.fetchall()
        if appoiments:
            response_body = [{
                'id_appoiment': appoiemt[0],
                'id_client': appoiemt[1],
                'id_supplier': appoiemt[2],
                'supplier_phone': appoiemt[3],
                'supplier_cp': appoiemt[4],
                'service_type': appoiemt[5],
                'note': appoiemt[6],
                'country': appoiemt[7],
                'city': appoiemt[8],
            } for appoiemt in appoiments]
            return response_body
        else:
            return {'error': 'No se encontraron citas'}