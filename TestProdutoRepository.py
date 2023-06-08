import unittest
import mysql.connector

def conectar_bd():
    connection = mysql.connector.connect(
        host=mysql://localhost:3306/bancodeteste,
        user=root,
        password=root,
        database=bancodeteste
    )
    return connection

def fechar_conexao_bd(connection):
    if connection.is_connected():
        connection.close()

class TestProduto(unittest.TestCase):

    produto_1 = "Produto 1"
    produto_2 = "Produto 2"
    tipo_1 = "Tipo 1"
    tipo_2 = "Tipo 2"

    def setUp(self):
        self.connection = conectar_bd()
        self.cursor = self.connection.cursor()
        create_table_query = """
            CREATE TABLE produtos (
                nome VARCHAR(255),
                tipo VARCHAR(255),
                quantidade INT
            )
        """
        self.cursor.execute(create_table_query)
        self.connection.commit()

    def tearDown(self):
        drop_table_query = "DROP TABLE produtos"
        self.cursor.execute(drop_table_query)
        self.connection.commit()
        fechar_conexao_bd(self.connection)

    def test_adicionar_produto_sucesso(self):
        resultado = adicionar_produto(self.produto_1, self.tipo_1, 10)
        self.assertTrue(resultado)

        query = "SELECT * FROM produtos WHERE nome = %s"
        self.cursor.execute(query, (self.produto_1,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], self.produto_1)
        self.assertEqual(result[1], self.tipo_1)
        self.assertEqual(result[2], 10)

    def test_adicionar_produto_duplicado(self):
        resultado = adicionar_produto(self.produto_2, self.tipo_1, 5)
        self.assertTrue(resultado)

        # Tentar adicionar o mesmo produto novamente
        resultado_duplicado = adicionar_produto(self.produto_2, self.tipo_2, 3)
        self.assertTrue(resultado_duplicado)

        query = "SELECT * FROM produtos WHERE nome = %s"
        self.cursor.execute(query, (self.produto_2,))
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0][0], self.produto_2)
        self.assertEqual(result[0][1], self.tipo_1)
        self.assertEqual(result[0][2], 5)

    def test_adicionar_produto_estoque_lotado(self):
        resultado = adicionar_produto(self.produto_1, self.tipo_1, 80)
        self.assertTrue(resultado)

        # Tentar adicionar mais produtos quando o estoque está lotado
        resultado_lotado = adicionar_produto(self.produto_2, self.tipo_2, 30)
        self.assertTrue(resultado_lotado)

        query = "SELECT * FROM produtos"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 1)

    def test_listar_produtos(self):
        resultado = listar_produtos()
        self.assertEqual(len(resultado), 0)

        adicionar_produto(self.produto_1, self.tipo_1, 10)
        adicionar_produto(self.produto_2, self.tipo_1, 5)

        resultado = listar_produtos()
        self.assertEqual(len(resultado), 2)
        self.assertIn((self.produto_1, self.tipo_1, 10), resultado)
        self.assertIn((self.produto_2, self.tipo_1, 5), resultado)

    def test_deletar_produto(self):
        adicionar_produto(self.produto_1, self.tipo_1, 10)
        adicionar_produto(self.produto_2, self.tipo_2, 5)

        resultado_anterior = listar_produtos()
        self.assertEqual(len(resultado_anterior), 2)

        resultado = deletar_produto(self.produto_1)
        self.assertTrue(resultado)

        query = "SELECT * FROM produtos WHERE nome = %s"
        self.cursor.execute(query, (self.produto_1,))
        result = self.cursor.fetchall()
        self.assertEqual(len(result), 0)

        resultado_atual = listar_produtos()
        self.assertEqual(len(resultado_atual), 1)
        self.assertNotIn((self.produto_1, self.tipo_1, 10), resultado_atual)

    def test_atualizar_produto(self):
        adicionar_produto(self.produto_1, self.tipo_1, 10)
        adicionar_produto(self.produto_2, self.tipo_1, 5)

        resultado_anterior = listar_produtos()
        self.assertEqual(len(resultado_anterior), 2)

        resultado = atualizar_produto(self.produto_1, "Novo Produto", "Novo Tipo", 20)
        self.assertTrue(resultado)

        query = "SELECT * FROM produtos WHERE nome = %s"
        self.cursor.execute(query, ("Novo Produto",))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], "Novo Produto")
        self.assertEqual(result[1], "Novo Tipo")
        self.assertEqual(result[2], 20)

        resultado_atual = listar_produtos()
        self.assertEqual(len(resultado_atual), 2)
        self.assertIn(("Novo Produto", "Novo Tipo", 20), resultado_atual)

    def test_listar_produto_especifico(self):
        adicionar_produto(self.produto_1, self.tipo_1, 10)
        adicionar_produto(self.produto_2, self.tipo_1, 5)

        resultado = listar_produto_especifico(self.produto_2)
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], self.produto_2)
        self.assertEqual(resultado[1], self.tipo_1)
        self.assertEqual(resultado[2], 5)

    def test_listar_produto_especifico_produto_nao_encontrado(self):
        resultado = listar_produto_especifico("Produto 3")
        self.assertIsNone(resultado)

if __name__ == "__main__":
    unittest.main()
