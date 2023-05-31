estoque = []

def adicionar_produto(nome, tipo, quantidade):
    if produto_ja_cadastrado(nome):
        return True

    if estoque_lotado(quantidade):
        return True
    
    novo_produto = {
        "nome": nome,
        "tipo": tipo, 
        "quantidade": quantidade
    }

    estoque.append(novo_produto)
    return True

def produto_ja_cadastrado(nome):
    for produto in estoque:
        if produto["nome"] == nome:
            return True
    return False

def estoque_lotado(quantidade):
    limite_estoque = 100
    quantidade_total = sum(produto["quantidade"] for produto in estoque)
    return quantidade_total + quantidade > limite_estoque

def listar_produtos():
    return estoque

def deletar_produto(nome):
    for produto in estoque:
        if produto["nome"] == nome:
            estoque.remove(produto)
            return True
    return False
