from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root1234',
    'database': 'citaexpress'
}

# Conectar a la base de datos
db = mysql.connector.connect(**db_config)
cursor = db.cursor()

@app.route('/api/clients', methods=['GET'])
def get_clients():
    cursor.execute("SELECT * FROM Clients")
    clients = cursor.fetchall()
    return jsonify({'clients': clients})

if __name__ == '__main__':
    app.run(debug=True)
