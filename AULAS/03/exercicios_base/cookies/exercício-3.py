# app.py
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    visitas = request.cookies.get("visitas")
    if visitas:
        visitas = int(visitas) + 1
        mensagem = f"Você já visitou {visitas} vezes."
    else:
        visitas = 1
        mensagem = "Bem-vindo pela primeira vez!"

    resp = make_response(mensagem)
    # TODO: atualizar cookie "visitas" com o novo valor
    return resp

if __name__ == '__main__':
    app.run(debug=True)