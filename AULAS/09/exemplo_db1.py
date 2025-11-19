# Adaptado de : https://www.geeksforgeeks.org/python-sqlite/
import sqlite3

try:
    # Criando e conectando ao banco, e criando um cursor
    conexao = sqlite3.connect('teste.db')
    cursor = conexao.cursor()
    print('Iniciando o banco')

    # Escrevendo uma query e executando
    query = 'select sqlite_version();'
    cursor.execute(query)

    # Pegando e mostrando o resultado
    resultado = cursor.fetchall()
    print(f'A versão do SQL é {resultado}')

    # Encerrando o cursor
    cursor.close()
except sqlite3.Error as erro:
    print('Ocorreu um erro: ', erro)
finally:
    # Encerrando a conexão com o banco de dados
    if conexao:
        conexao.close()
        print('Conexão encerrada')