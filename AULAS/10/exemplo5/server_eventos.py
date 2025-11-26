from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)

# Para requisições assíncronas de um HTML local
#   Política de segurança: CORS (Cross-Origin Resource Sharing)
#   bloqueia requisições cross-origin.
CORS(app)

db_path = 'AULAS/10/exemplo5/eventos.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS eventos
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, data TEXT, descricao TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/eventos', methods=['GET'])
def get_eventos():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM eventos ORDER BY data ASC')
    eventos = [{'id': row[0], 'nome': row[1], 'data': row[2], 'descricao': row[3]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(eventos)

@app.route('/eventos', methods=['POST'])
def add_event():
    data = request.json
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO eventos (nome, data, descricao) VALUES (?, ?, ?)', 
                   (data['nome'], data['data'], data['descricao']))
    conn.commit()
    event_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': event_id, 'nome': data['nome'], 'data': data['data'], 'descricao': data['descricao']}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5005)