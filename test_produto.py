import unittest
from produto import adicionar_produto, listar_produtos, deletar_produto

class TestProduto(unittest.TestCase):

    produto_1 = "Produto 1"
    produto_2 = "Produto 2"
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
        self.assertEqual(len(resultado), 1)
        self.assertIn({"nome": self.produto_2, "tipo": self.tipo_1, "quantidade": 5}, resultado)

    def test_deletar_produto(self):
        # Teste: Remover um produto do estoque
        resultado_anterior = listar_produtos()
        self.assertEqual(len(resultado_anterior), 2)

        resultado = deletar_produto(self.produto_1)
        self.assertTrue(resultado)

        resultado_atual = listar_produtos()
        self.assertEqual(len(resultado_atual), 1)
        self.assertNotIn({"nome": "Produto 1", "tipo": "Tipo 1", "quantidade": 10}, resultado_atual)