import unittest
from cadastro import CadastroAlunos


class TestCadastroAlunos(unittest.TestCase):
    def setUp(self):
        self.cadastro = CadastroAlunos()

    def test_adicionar_e_listar_aluno(self):
        self.cadastro.adicionar("Ana Souza", "A001")
        self.assertEqual(
            self.cadastro.listar(),
            [{"nome": "Ana Souza", "matricula": "A001"}],
        )

    def test_nao_permite_nome_vazio(self):
        with self.assertRaises(ValueError):
            self.cadastro.adicionar("  ", "A001")

    def test_nao_permite_matricula_duplicada(self):
        self.cadastro.adicionar("Ana Souza", "A001")
        with self.assertRaises(ValueError):
            self.cadastro.adicionar("Bruno Lima", "A001")

    def test_remover_aluno(self):
        self.cadastro.adicionar("Ana Souza", "A001")
        self.assertTrue(self.cadastro.remover("A001"))
        self.assertEqual(self.cadastro.listar(), [])

    def test_remover_matricula_inexistente(self):
        self.assertFalse(self.cadastro.remover("NAO-EXISTE"))


if __name__ == "__main__":
    unittest.main()
