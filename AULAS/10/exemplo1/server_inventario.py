from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)

# Para requisições assíncronas de um HTML local
#   Política de segurança: CORS (Cross-Origin Resource Sharing)
#   bloqueia requisições cross-origin.
CORS(app)

db_path = 'AULAS/10/exemplo1/inventario.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventario
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, quantidade INTEGER, preco REAL)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/inventario', methods=['GET'])
def get_inventory():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventario')
    items = [{'id': row[0], 'nome': row[1], 'quantidade': row[2], 'preco': row[3]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(items)

@app.route('/inventario', methods=['POST'])
def add_item():
    data = request.json
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO inventario (nome, quantidade, preco) VALUES (?, ?, ?)', 
                   (data['nome'], data['quantidade'], data['preco']))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': item_id, 'nome': data['nome'], 'quantidade': data['quantidade'], 'preco': data['preco']}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)