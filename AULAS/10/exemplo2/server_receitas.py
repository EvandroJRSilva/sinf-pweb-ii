from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)

# Para requisições assíncronas de um HTML local
#   Política de segurança: CORS (Cross-Origin Resource Sharing)
#   bloqueia requisições cross-origin.
CORS(app)

db_path = 'AULAS/10/exemplo2/receitas.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS receitas
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, ingredientes TEXT, instrucoes TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/receitas', methods=['GET'])
def get_recipes():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM receitas')
    receitas = [{'id': row[0], 'nome': row[1], 'ingredientes': row[2], 'instrucoes': row[3]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(receitas)

@app.route('/receitas', methods=['POST'])
def add_recipe():
    data = request.json
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO receitas (nome, ingredientes, instrucoes) VALUES (?, ?, ?)', 
                   (data['nome'], data['ingredientes'], data['instrucoes']))
    conn.commit()
    recipe_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': recipe_id, 'nome': data['nome'], 'ingredientes': data['ingredientes'], 'instrucoes': data['instrucoes']}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)