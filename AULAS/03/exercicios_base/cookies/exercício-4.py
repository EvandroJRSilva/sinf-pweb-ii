# app.py
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    idioma = request.cookies.get("idioma")
    if idioma:
        if idioma == "pt":
            return "Bem-vindo de volta!"
        elif idioma == "en":
            return "Welcome back!"
    else:
        resp = make_response("Idioma não definido. Definindo como português.")
        # TODO: definir cookie idioma = "pt"
        return resp

if __name__ == '__main__':
    app.run(debug=True)