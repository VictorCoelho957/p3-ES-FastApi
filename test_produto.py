import unittest
from produto import adicionar_produto, listar_produtos

class TestAdicionarProduto(unittest.TestCase):

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
        self.assertEqual(len(resultado), 2)
        self.assertIn({"nome": self.produto_1, "tipo": self.tipo_1, "quantidade": 10}, resultado)
        self.assertIn({"nome": self.produto_2, "tipo": self.tipo_1, "quantidade": 5}, resultado)