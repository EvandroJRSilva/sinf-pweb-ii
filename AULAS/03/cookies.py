from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    usuario = request.cookies.get('usuario')
    if usuario:
        return f"Bem-vindo de volta, {usuario}!"
    else:
        resp = make_response("Olá, novo visitante! Definindo cookie...")
        resp.set_cookie('usuario', 'Alice', max_age=60*60*24*7)  # 7 dias
        return resp

if __name__ == '__main__':
    app.run(debug=True)
