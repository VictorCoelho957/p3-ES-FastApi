import unittest
from produto import adicionar_produto

class TestProduto(unittest.TestCase):
    def test_adicionar_produto_sucesso(self):
        # Teste: Adicionar um novo produto ao estoque com sucesso
        resultado = adicionar_produto("Produto 1", "Tipo 1", 10)
        self.assertTrue(resultado)

    def test_adicionar_produto_duplicado(self):
        # Teste: Tentar adicionar um produto já existente no estoque
        resultado = adicionar_produto("Produto 2", "Tipo 1", 5)
        self.assertTrue(resultado)
        print(resultado)

    def test_adicionar_produto_estoque_lotado(self):
        # Teste: Tentar adicionar um produto quando o estoque estiver cheio
        resultado = adicionar_produto("Produto 2", "Tipo 2", 100)
        self.assertTrue(resultado)