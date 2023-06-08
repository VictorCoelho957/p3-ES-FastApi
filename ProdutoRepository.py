import mysql.connector

# Função para estabelecer a conexão com o banco de dados
def conectar_bd():
    connection = mysql.connector.connect(
        host=mysql://localhost:3306/bancodeteste,
        user=root,
        password=root,
        database=bancodeteste
    )
    return connection

# Função para fechar a conexão com o banco de dados
def fechar_conexao_bd(connection):
    if connection.is_connected():
        connection.close()

# Função para adicionar um produto ao banco de dados
def adicionar_produto(nome, tipo, quantidade):
    connection = conectar_bd()
    cursor = connection.cursor()

    if produto_ja_cadastrado(cursor, nome):
        fechar_conexao_bd(connection)
        return True

    if estoque_lotado(cursor, quantidade):
        fechar_conexao_bd(connection)
        return True
    
    query = "INSERT INTO produtos (nome, tipo, quantidade) VALUES (%s, %s, %s)"
    values = (nome, tipo, quantidade)
    cursor.execute(query, values)
    connection.commit()

    fechar_conexao_bd(connection)

    return True

# Função para verificar se um produto já está cadastrado no banco de dados
def produto_ja_cadastrado(cursor, nome):
    query = "SELECT nome FROM produtos WHERE nome = %s"
    cursor.execute(query, (nome,))
    result = cursor.fetchone()
    if result is not None:
        return True
    return False

# Função para verificar se o estoque está lotado
def estoque_lotado(cursor, quantidade):
    limite_estoque = 100
    query = "SELECT SUM(quantidade) FROM produtos"
    cursor.execute(query)
    total_quantidade = cursor.fetchone()[0]
    if total_quantidade is not None and total_quantidade + quantidade > limite_estoque:
        return True
    return False

# Função para listar todos os produtos do banco de dados
def listar_produtos():
    connection = conectar_bd()
    cursor = connection.cursor()

    query = "SELECT * FROM produtos"
    cursor.execute(query)
    produtos = cursor.fetchall()

    fechar_conexao_bd(connection)

    return produtos

# Função para deletar um produto do banco de dados
def deletar_produto(nome):
    connection = conectar_bd()
    cursor = connection.cursor()

    query = "DELETE FROM produtos WHERE nome = %s"
    cursor.execute(query, (nome,))
    row_count = cursor.rowcount

    connection.commit()
    fechar_conexao_bd(connection)

    if row_count > 0:
        return True
    return False

# Função para atualizar os dados de um produto no banco de dados
def atualizar_produto(nome, novo_nome, novo_tipo, nova_quantidade):
    connection = conectar_bd()
    cursor = connection.cursor()

    query = "UPDATE produtos SET nome = %s, tipo = %s, quantidade = %s WHERE nome = %s"
    values = (novo_nome, novo_tipo, nova_quantidade, nome)
    cursor.execute(query, values)
    row_count = cursor.rowcount

    connection.commit()
    fechar_conexao_bd(connection)

    if row_count > 0:
        return True
    return False

# Função para listar as informações de um produto específico
def listar_produto_especifico(nome):
    connection = conectar_bd()
    cursor = connection.cursor()

    query = "SELECT * FROM produtos WHERE nome = %s"
    cursor.execute(query, (nome,))
    produto = cursor.fetchone()

    fechar_conexao_bd(connection)

    if produto:
        produto_especifico = {
            "nome": produto[0],
            "tipo": produto[1],
            "quantidade": produto[2]
        }
        return produto_especifico

    return None
