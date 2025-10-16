# Exemplo introdutório de validação no lado do servidor
def validar_idade(idade_str):
    """Garante que a entrada é um número inteiro positivo."""
    try:
        idade = int(idade_str)
        if idade > 0 and idade < 120:
            return True, "Idade válida."
        else:
            return False, "A idade deve estar entre 1 e 119."
    except ValueError:
        return False, "A idade deve ser um número."

# Testes
print(f"25: {validar_idade('25')}")
print(f"'abc': {validar_idade('abc')}")
print(f"-5: {validar_idade('-5')}")