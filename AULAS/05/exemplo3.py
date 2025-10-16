# Módulo de Banco de Dados (exemplo conceitual)
class Database:
    def execute(self, query):
        # Apenas simula a execução
        print(f"Executando SQL: {query}")

db = Database()
username_entrada = "user_normal"
password_entrada = "' OR '1'='1" # Payload de Ataque Comum!

# --- 1. CÓDIGO VULNERÁVEL (Concatenando a string) ---
# A query final fica: "SELECT * FROM users WHERE username = 'user_normal' AND password = '' OR '1'='1'"
# O 'OR 1=1' faz o WHERE ser TRUE para qualquer linha, permitindo o login sem senha.
vulnerable_query = f"SELECT * FROM users WHERE username = '{username_entrada}' AND password = '{password_entrada}';"
print("--- 1. CÓDIGO VULNERÁVEL ---")
db.execute(vulnerable_query)


# --- 2. CÓDIGO SEGURO (Consultas Parametrizadas) ---
# A query é passada separada dos dados. O banco trata a entrada como VALOR de campo.
# O payload inteiro (' OR '1'='1) é tratado como a senha que o usuário está procurando, o que falhará.
secure_query = "SELECT * FROM users WHERE username = %s AND password = %s;"
parametros = (username_entrada, password_entrada)

print("\n--- 2. CÓDIGO SEGURO (Consultas Parametrizadas) ---")
print(f"SQL a ser executado: {secure_query}")
print(f"Parâmetros: {parametros}")
# O módulo de banco de dados se encarrega de garantir que os parâmetros sejam escapados.