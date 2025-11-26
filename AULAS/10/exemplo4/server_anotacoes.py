from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS

app = Flask(__name__)

# Para requisições assíncronas de um HTML local
#   Política de segurança: CORS (Cross-Origin Resource Sharing)
#   bloqueia requisições cross-origin.
CORS(app)

db_path = 'AULAS/10/exemplo4/anotacoes.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS anotacoes
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT, conteudo TEXT)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/anotacoes', methods=['GET'])
def get_anotacoes():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM anotacoes')
    anotacoes = [{'id': row[0], 'titulo': row[1], 'conteudo': row[2]} for row in cursor.fetchall()]
    conn.close()
    return jsonify(anotacoes)

@app.route('/anotacoes', methods=['POST'])
def add_note():
    data = request.json
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO anotacoes (titulo, conteudo) VALUES (?, ?)', (data['titulo'], data['conteudo']))
    conn.commit()
    note_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': note_id, 'titulo': data['titulo'], 'conteudo': data['conteudo']}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5004)