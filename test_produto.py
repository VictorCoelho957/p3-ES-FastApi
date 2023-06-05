import unittest
from produto import adicionar_produto, listar_produtos, deletar_produto, atualizar_produto, listar_produto_especifico

class TestProduto(unittest.TestCase):

    produto_1 = "Produto 1"
    produto_2 = "Produto 2"
    produto_3 = "Produto 3"
    tipo_1 = "Tipo 1"
    tipo_2 = "Tipo 2"

    def test_adicionar_produto_sucesso(self):
        # Teste: Adicionar um novo produto ao estoque com sucesso
        resultado = adicionar_produto( self.produto_1, self.tipo_1, 10)
        self.assertTrue(resultado)

    def test_adicionar_produto_duplicado(self):
        # Teste: Tentar adicionar um produto já existente no estoque
        resultado = adicionar_produto(self.produto_2, self.tipo_1, 5)
        self.assertTrue(resultado)

    def test_adicionar_produto_estoque_lotado(self):
        # Teste: Tentar adicionar um produto quando o estoque estiver cheio
        resultado = adicionar_produto(self.produto_2, self.tipo_2, 100)
        self.assertTrue(resultado)

    def test_listar_produtos(self):
        # Teste: Listar todos os produtos cadastrados
        resultado = listar_produtos()
        self.assertEqual(len(resultado), 2)
        self.assertIn({"nome": self.produto_2, "tipo": self.tipo_1, "quantidade": 5}, resultado)

    def test_deletar_produto(self):
        # Teste: Remover um produto do estoque
        resultado_anterior = listar_produtos()
        self.assertEqual(len(resultado_anterior), 2)

        resultado = deletar_produto(self.produto_1)
        self.assertTrue(resultado)

        resultado_atual = listar_produtos()
        self.assertEqual(len(resultado_atual), 1)
        self.assertNotIn({"nome": self.produto_1, "tipo": self.tipo_1, "quantidade": 10}, resultado_atual)

    def test_atualizar_produto(self):
        # Teste: Atualizar informações de um produto no estoque
        resultado_anterior = listar_produtos()
        self.assertEqual(len(resultado_anterior), 2)

        resultado = atualizar_produto(self.produto_1, "Novo Produto", "Novo Tipo", 20)
        self.assertTrue(resultado)

        resultado_atual = listar_produtos()
        self.assertEqual(len(resultado_atual), 2)
        produto_atualizado = {"nome": "Novo Produto", "tipo": "Novo Tipo", "quantidade": 20}
        self.assertIn(produto_atualizado, resultado_atual)

    def test_listar_produto_especifico(self):
        # Teste: Exibir informações de um produto específico
        resultado = listar_produto_especifico(self.produto_2)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado["nome"], self.produto_2)
        self.assertEqual(resultado["tipo"], self.tipo_1)
        self.assertEqual(resultado["quantidade"], 5)

    def test_listar_produto_especifico_produto_nao_encontrado(self):
        # Teste: Tentar exibir informações de um produto que não existe no estoque
        resultado = listar_produto_especifico(self.produto_3)
        self.assertIsNone(resultado)
