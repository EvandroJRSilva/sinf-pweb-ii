import secrets

# No servidor, ao gerar o formulário
def gerar_token_csrf():
    return secrets.token_hex(16) # Gera um token aleatório

# Token é inserido no formulário (campo hidden)
token_atual = gerar_token_csrf()
# <input type="hidden" name="csrf_token" value="{{ token_atual }}">

# No servidor, ao receber a requisição
def processar_requisicao(token_recebido, token_na_sessao):
    if token_recebido == token_na_sessao:
        print("Requisição VÁLIDA: Tokens correspondem. Ação executada.")
        return True
    else:
        print("Requisição INVÁLIDA (CSRF provável): Tokens NÃO correspondem.")
        return False

# Teste (Sucesso)
print(processar_requisicao(token_atual, token_atual))

# Teste (Falha - O token do atacante seria NULO ou FALSO)
print(processar_requisicao("token_falso", token_atual))