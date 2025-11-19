# Adaptado de: https://pythonclub.com.br/gerenciando-banco-dados-sqlite3-python-parte1.html
import sqlite3

try:
    # Conectando
    conexao = sqlite3.connect('AULAS/09/teste.db')
    print('Conexão bem sucedida')

    # Definindo um cursor
    cursor = conexao.cursor()
    
    # Criando a tabela (schema)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL,
        fone TEXT,
        cidade TEXT,
        uf VARCHAR(2) NOT NULL,
        criado_em DATE NOT NULL
    );
    """)

    print('Tabela criada com sucesso')

    # Inserindo alguns registros
    cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Fulano', 35, '00000000000', 'fulano@estacio.br', '(86)99999-9999', 'Teresina', 'PI', '2023-03-24')
    """)

    cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Cicrano', 87, '11111111111', 'cicrano@email.com', '98765-4321', 'São Paulo', 'SP', '2023-03-25')
    """)

    cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Beltrana', 21, '22222222222', 'beltana@email.com', '98-98765-4322', 'Caxias', 'MA', '2023-03-24')
    """)

    cursor.execute("""
        INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
        VALUES ('Derpina', 19, '33333333333', 'derpina@meme.com', '11-98765-4323', 'Campinas', 'SP', '2023-03-25')
    """)

    # Gravando no Banco
    conexao.commit()
    print('Dados inseridos com sucesso')

    cursor.close()
except sqlite3.Error as erro:
    print('Ocorreu um erro: ', erro)
    conexao.rollback()
finally:
    # Encerrando a conexão com o banco de dados
    if conexao:
        conexao.close()
        print('Conexão encerrada')