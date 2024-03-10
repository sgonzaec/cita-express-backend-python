import psycopg2

class LocationService:
    def __init__(self, db_config):
        self.db = psycopg2.connect(**db_config)
        self.cursor = self.db.cursor()

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