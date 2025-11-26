from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

# Para requisições assíncronas de um HTML local
#   Política de segurança: CORS (Cross-Origin Resource Sharing)
#   bloqueia requisições cross-origin.
CORS(app)

db_path = 'AULAS/10/exemplo3/fitness.db'

def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS treino
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT, exercicio TEXT, duracao INTEGER)''')
    conn.commit()
    conn.close()

init_db()

@app.route('/treino', methods=['GET'])
def get_workouts():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM treino')
    treino = [{'id': row[0], 'data': row[1], 'exercicio': row[2], 'duracao': row[3]} for row in cursor.fetchall()]
    total = sum(w['duracao'] for w in treino)
    conn.close()
    return jsonify({'treino': treino, 'total_horas': total})

@app.route('/treino', methods=['POST'])
def add_workout():
    data = request.json
    data['data'] = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO treino (data, exercicio, duracao) VALUES (?, ?, ?)', 
                   (data['data'], data['exercicio'], data['duracao']))
    conn.commit()
    conn.close()
    return jsonify(data), 201

if __name__ == '__main__':
    app.run(debug=True, port=5003)