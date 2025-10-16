# para criar senhas aleatórias
import secrets  
# para letras e dígitos ASCII
import string   
# para gerar hash com a senha
import hashlib  
# para esconder o senha passada no input pelo terminal
from getpass import getpass 

USER_DETAILS_FILEPATH = "./users.txt"

# símbolos de pontuação que podem ser usados na geração de senha
PUNCTUATIONS = "@#$%&"

DEFAULT_PASSWORD_LENGTH = 12

INVALID_LENGTH_MESSAGE = f'''
A senha deve ter um comprimento entre 8 e 16 caracteres. 
O comprimento da senha deve ser um número.
Gerando uma senha com o comprimento padrão de {DEFAULT_PASSWORD_LENGTH} caracteres.
'''


def generate_password(length=12):
    """
    Gera uma senha aleatória de tamanho length. A senha consiste em um conjunto contendo letras e dígitos ASCII e caracteres de pontuação.
    """
    characters = string.ascii_letters + string.digits + PUNCTUATIONS
    pwd = ''.join(secrets.choice(characters) for _ in range(length))
    return pwd


def hash_password(pwd:str):
    """
    Cria o hash de uma senha usando o algoritmo SHA-256
    """
    pwd_bytes = pwd.encode('utf-8')
    hashed_pwd = hashlib.sha256(pwd_bytes).hexdigest()
    return hashed_pwd


def save_user(username, hashed_pwd):
    """
    Salva usuário e hash de senha em um arquivo.
    """
    with open(USER_DETAILS_FILEPATH, "a") as f:
        f.write(f"{username} {hashed_pwd}\n")


def user_exists(username:str):
    """
    Verifica se um dado usuário já foi criado.
    """
    try:
        with open(USER_DETAILS_FILEPATH, "r") as f:
            for line in f:
                parts = line.split()
                if parts[0] == username:
                    return True
    except FileNotFoundError as fl_err:
        print(f"{fl_err.args[-1]}: {USER_DETAILS_FILEPATH}")
        print(f"O sistema criará o arquivo: {USER_DETAILS_FILEPATH}")
    return False


def authenticate_user(username:str, password:str):
    """
    Verifica se o hash de uma senha coincide com o hash armazenado para o usuário fornecido.
    """
    with open(USER_DETAILS_FILEPATH, "r") as f:
        for line in f:
            parts = line.split()
            if parts[0] == username:
                hashed_password = parts[1]
                if hashed_password == hash_password(password):
                    return True
                else:
                    return False
    return False


def validate_input(password_length):
    """
    Valida o comprimento da senha, para garantir que a senha terá entre 8 e 16 (incluso) caracteres.
    """
    try:
        password_length = int(password_length)
        if password_length < 8 or password_length > 16:
            raise ValueError("A senha deve ter entre 8 e 16 caracteres")
        return password_length
    except ValueError:
        print(INVALID_LENGTH_MESSAGE)
        return DEFAULT_PASSWORD_LENGTH


def register():
    """
    Função para registro de novo usuário.
    """
    username = input("Insira seu nome de usuário: ")
    if user_exists(username):
        print("Nome de usuário já existe.")
        return
    length = input("Insira o comprimento da senha a ser gerada automaticamente (Número 8-16): ")
    length = validate_input(length)
    password = generate_password(length)

    hashed_password = hash_password(password)
    save_user(username, hashed_password)
    print("Usuário criado com sucesso.")
    print("Sua senha é:", password)


def login():
    username = input("Insira seu nome de usuário: ")
    if not user_exists(username):
        print("Nome de usuário inexistente.")
        return

    password = getpass("Senha: ")
    if not authenticate_user(username, password):
        print("Senha incorreta.")
        return
    print("Login feito com sucesso.")


def main():
    while True:
        print("1. Registrar\n2. Login\n3. Sair")
        choice = input("Insira a opção escolhida: ")
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

# TODO: continuar desse site 
# https://rs-punia.medium.com/designing-a-login-register-and-user-authentication-script-in-python-326a11821504