from flask import Flask, render_template, request

# Como rodar:
#   Executar o servidor Python com o comando: python app.py
#   Acessar http://127.0.0.1:5000 pelo navegador

app = Flask(__name__)

@app.route('/')
def index():
    # A rota raiz apenas renderiza o arquivo HTML
    #   AJAX
    return render_template('ajax-index.html')
    #   Fetch API
    # return render_template('fetch-index.html')

@app.route('/processar', methods=['POST'])
def processar_dados():
    # Verifica se a requisição foi do tipo POST
    if request.method == 'POST':
        # Acessa os dados do formulário
        nome = request.form.get('nome', 'Nome não fornecido')
        email = request.form.get('email', 'E-mail não fornecido')

        # Retorna uma resposta de texto para o cliente
        return f"Dados recebidos com sucesso!\nNome: {nome}\nE-mail: {email}"

    # Se não for POST, retorna uma mensagem de erro
    return "Método de requisição inválido.", 405

if __name__ == '__main__':
    app.run(debug=True)